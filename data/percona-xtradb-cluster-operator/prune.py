import input

custom_fields = [
    input.ProblematicField(['spec', 'pmm']),
    input.ProblematicField(['spec', 'backup']),
    input.ProblematicField(['spec', 'proxysql']),
    input.ProblematicField(['spec', 'updateStrategy']),
    input.ProblematicField(['spec', 'upgradeOptions']),
    input.ProblematicField(['spec', 'allowUnsafeConfigurations']),

    input.CopiedOverField(['spec', 'haproxy', 'affinity', 'advanced']),
    input.CopiedOverField(['spec', 'haproxy', 'containerSecurityContext']),
    input.CopiedOverField(['spec', 'haproxy', 'podSecurityContext']),
    input.CopiedOverField(['spec', 'haproxy', 'livenessProbes']),
    input.CopiedOverField(['spec', 'haproxy', 'readinessProbes']),
    input.CopiedOverField(['spec', 'haproxy', 'resources'], used_fields=[
        ['spec', 'haproxy', 'resources', 'limits'],
        ['spec', 'haproxy', 'resources', 'requests'],
    ]),
    input.CopiedOverField(['spec', 'haproxy', 'sidecars'], array=True),
    input.OverSpecifiedField(['spec', 'haproxy', 'sidecarVolumes'], array=True),
    input.OverSpecifiedField(['spec', 'haproxy', 'sidecarPVCs'], array=True),
    input.CopiedOverField(['spec', 'haproxy', 'tolerations'], array=True),
    input.CopiedOverField(['spec', 'haproxy', 'volumeSpec', 'emptyDir']),
    input.CopiedOverField(['spec', 'haproxy', 'volumeSpec', 'hostPath']),
    input.CopiedOverField(['spec', 'haproxy', 'volumeSpec', 'persistentVolumeClaim']),

    input.CopiedOverField(['spec', 'logcollector', 'containerSecurityContext']),
    input.CopiedOverField(['spec', 'logcollector', 'resources']),

    input.CopiedOverField(['spec', 'proxysql', 'affinity', 'advanced']),
    input.CopiedOverField(['spec', 'proxysql', 'containerSecurityContext']),
    input.CopiedOverField(['spec', 'proxysql', 'livenessProbes']),
    input.CopiedOverField(['spec', 'proxysql', 'readinessProbes']),
    input.CopiedOverField(['spec', 'proxysql', 'resources'], used_fields=[
        ['spec', 'proxysql', 'resources', 'limits'],
        ['spec', 'proxysql', 'resources', 'requests'],
    ]),
    input.CopiedOverField(['spec', 'proxysql', 'tolerations'], array=True),
    input.CopiedOverField(['spec', 'proxysql', 'sidecars'], array=True),
    input.OverSpecifiedField(['spec', 'proxysql', 'sidecarVolumes'], array=True),
    input.OverSpecifiedField(['spec', 'proxysql', 'sidecarPVCs'], array=True),
    input.CopiedOverField(['spec', 'proxysql', 'volumeSpec', 'emptyDir']),
    input.CopiedOverField(['spec', 'proxysql', 'volumeSpec', 'hostPath']),
    input.CopiedOverField(['spec', 'proxysql', 'volumeSpec', 'persistentVolumeClaim']),

    input.CopiedOverField(['spec', 'pxc', 'affinity', 'advanced']),
    input.CopiedOverField(['spec', 'pxc', 'containerSecurityContext']),
    input.CopiedOverField(['spec', 'pxc', 'podSecurityContext']),
    input.CopiedOverField(['spec', 'pxc', 'resources'], used_fields=[
        ['spec', 'pxc', 'resources', 'requests'],
        ['spec', 'pxc', 'resources', 'limits'],
    ]),
    input.CopiedOverField(['spec', 'pxc', 'livenessProbes']),
    input.CopiedOverField(['spec', 'pxc', 'readinessProbes']),
    input.CopiedOverField(['spec', 'pxc', 'tolerations'], array=True),
    input.CopiedOverField(['spec', 'pxc', 'sidecars'], array=True),
    input.OverSpecifiedField(['spec', 'pxc', 'sidecarVolumes'], array=True),
    input.OverSpecifiedField(['spec', 'pxc', 'sidecarPVCs'], array=True),
    input.CopiedOverField(['spec', 'pxc', 'volumeSpec', 'emptyDir']),
    input.CopiedOverField(['spec', 'pxc', 'volumeSpec', 'hostPath']),
    input.CopiedOverField(['spec', 'pxc', 'volumeSpec', 'persistentVolumeClaim']),
]
