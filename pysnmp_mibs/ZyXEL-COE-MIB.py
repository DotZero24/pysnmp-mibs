#
# PySNMP MIB module ZyXEL-COE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZyXEL-COE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZyXEL-COE-MIB", overheatOver=overheatOver, DisplayString=DisplayString, zyxel=zyxel, dslam=dslam, zysam_1000=zysam_1000, p2100=p2100, p1600=p1600, mtu=mtu, zysam_1200=zysam_1200, pes_100=pes_100, problemCause=problemCause, prestige=prestige, zysam_1100=zysam_1100, shes_100=shes_100, ves_100=ves_100, systemShutdown=systemShutdown, systemTraps=systemTraps, products=products, reboot=reboot, p1400=p1400, aes_100=aes_100, aes_100_1=aes_100_1, overheat=overheat, zysam_2000=zysam_2000, systemTemperature=systemTemperature)
