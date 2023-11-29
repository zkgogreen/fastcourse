from user.models import UserCourse, UserBab
from teacher.models import Kelas, Bab, Pelajaran, UserLesson


def bab_navigate(request, slug, urutan_bab, urutan_pelajaran, isPelajaran=True):
    context = {}
    kelas = Kelas.objects.get(slug=slug)
    bab = Bab.objects.filter(kelas=kelas)
    pelajarans = Pelajaran.objects.filter(kelas=kelas)
    pelajaran = pelajarans.get(urutan=urutan_pelajaran, bab_kelas=bab.get(urutan=urutan_bab))
    history = UserCourse.objects.get(kelas=kelas, user=request.user)


    userlesson = UserLesson.objects.filter(user=request.user, kelas=kelas, bab_kelas=pelajaran.bab_kelas)
    userbab = UserBab.objects.filter(user=request.user, kelas=kelas)

    context['bab'] = userbab
    context['hasPrev'] = pelajaran.prev(isPelajaran)
    context['hasNext'] = pelajaran.next(isPelajaran)
    context['pelajaran'] = pelajaran
    context['history'] = history
    context['soal'] = pelajaran.soal()
    context['komentar'] = pelajaran.komentar()

    userlesson.filter(pelajaran=pelajaran).update(isdone=True)
    history.bab_kelas = pelajaran.bab_kelas
    history.pelajaran = pelajaran
    history.save()

    return context
