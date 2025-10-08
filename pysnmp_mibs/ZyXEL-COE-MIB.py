#
# PySNMP MIB module ZyXEL-COE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZyXEL-COE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "PhysAddress")
class DisplayString(OctetString):
    pass

zyxel = MibIdentifier((1, 3, 6, 1, 4, 1, 890))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1))
prestige = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 2))
mtu = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3))
dslam = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 4))
systemTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 999))
aes_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 1)).setLabel("aes-100")
pes_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 2)).setLabel("pes-100")
ves_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 3)).setLabel("ves-100")
shes_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 4)).setLabel("shes-100")
p1600 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 5))
p1400 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 6))
p2100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 7))
aes_100_1 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 8)).setLabel("aes-100-1")
zysam_1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 4, 1)).setLabel("zysam-1000")
zysam_1100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 4, 2)).setLabel("zysam-1100")
zysam_1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 4, 3)).setLabel("zysam-1200")
zysam_2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 4, 4)).setLabel("zysam-2000")
problemCause = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 999, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: problemCause.setStatus('mandatory')
systemTemperature = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 999, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTemperature.setStatus('mandatory')
reboot = NotificationType((1, 3, 6, 1, 4, 1, 890) + (0,1)).setObjects(("ZyXEL-COE-MIB", "problemCause"))
systemShutdown = NotificationType((1, 3, 6, 1, 4, 1, 890) + (0,2)).setObjects(("ZyXEL-COE-MIB", "problemCause"))
overheat = NotificationType((1, 3, 6, 1, 4, 1, 890) + (0,3)).setObjects(("ZyXEL-COE-MIB", "systemTemperature"))
overheatOver = NotificationType((1, 3, 6, 1, 4, 1, 890) + (0,4)).setObjects(("ZyXEL-COE-MIB", "systemTemperature"))
mibBuilder.exportSymbols("ZyXEL-COE-MIB", dslam=dslam, p1400=p1400, p2100=p2100, aes_100=aes_100, shes_100=shes_100, overheatOver=overheatOver, zysam_1200=zysam_1200, aes_100_1=aes_100_1, p1600=p1600, reboot=reboot, overheat=overheat, ves_100=ves_100, problemCause=problemCause, systemTraps=systemTraps, pes_100=pes_100, systemShutdown=systemShutdown, zyxel=zyxel, zysam_1000=zysam_1000, products=products, prestige=prestige, zysam_1100=zysam_1100, DisplayString=DisplayString, systemTemperature=systemTemperature, mtu=mtu, zysam_2000=zysam_2000)
