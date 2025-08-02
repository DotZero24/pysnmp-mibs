_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
samsung=ModuleIdentity((1,3,6,1,4,1,236))
_Division_ObjectIdentity=ObjectIdentity
division=_Division_ObjectIdentity((1,3,6,1,4,1,236,11))
if mibBuilder.loadTexts:division.setStatus(_A)
_Oadivision_ObjectIdentity=ObjectIdentity
oadivision=_Oadivision_ObjectIdentity((1,3,6,1,4,1,236,11,5))
if mibBuilder.loadTexts:oadivision.setStatus(_A)
_SamsungCommonMIB_ObjectIdentity=ObjectIdentity
samsungCommonMIB=_SamsungCommonMIB_ObjectIdentity((1,3,6,1,4,1,236,11,5,11))
if mibBuilder.loadTexts:samsungCommonMIB.setStatus(_A)
mibBuilder.exportSymbols('SAMSUNG-COMMON-MIB',**{'samsung':samsung,'division':division,'oadivision':oadivision,'samsungCommonMIB':samsungCommonMIB})