_F='h3cPBRNexthopAddr'
_E='h3cPBRNexthopAddrType'
_D='accessible-for-notify'
_C='TruthValue'
_B='A3COM-HUAWEI-PBR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_C)
h3cPBR=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,113))
if mibBuilder.loadTexts:h3cPBR.setRevisions(('2010-12-10 15:58',))
_H3cPBRObjects_ObjectIdentity=ObjectIdentity
h3cPBRObjects=_H3cPBRObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,113,1))
_H3cPBRGlobal_ObjectIdentity=ObjectIdentity
h3cPBRGlobal=_H3cPBRGlobal_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,113,1,1))
class _H3cPBRNexthopTrapEnabled_Type(TruthValue):defaultValue=2
_H3cPBRNexthopTrapEnabled_Type.__name__=_C
_H3cPBRNexthopTrapEnabled_Object=MibScalar
h3cPBRNexthopTrapEnabled=_H3cPBRNexthopTrapEnabled_Object((1,3,6,1,4,1,43,45,1,10,2,113,1,1,1),_H3cPBRNexthopTrapEnabled_Type())
h3cPBRNexthopTrapEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cPBRNexthopTrapEnabled.setStatus(_A)
_H3cPBRMibTrap_ObjectIdentity=ObjectIdentity
h3cPBRMibTrap=_H3cPBRMibTrap_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,113,1,2))
_H3cPBRTrapObjects_ObjectIdentity=ObjectIdentity
h3cPBRTrapObjects=_H3cPBRTrapObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,113,1,2,1))
_H3cPBRNexthopAddrType_Type=InetAddressType
_H3cPBRNexthopAddrType_Object=MibScalar
h3cPBRNexthopAddrType=_H3cPBRNexthopAddrType_Object((1,3,6,1,4,1,43,45,1,10,2,113,1,2,1,1),_H3cPBRNexthopAddrType_Type())
h3cPBRNexthopAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPBRNexthopAddrType.setStatus(_A)
_H3cPBRNexthopAddr_Type=InetAddress
_H3cPBRNexthopAddr_Object=MibScalar
h3cPBRNexthopAddr=_H3cPBRNexthopAddr_Object((1,3,6,1,4,1,43,45,1,10,2,113,1,2,1,2),_H3cPBRNexthopAddr_Type())
h3cPBRNexthopAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cPBRNexthopAddr.setStatus(_A)
_H3cPBRTraps_ObjectIdentity=ObjectIdentity
h3cPBRTraps=_H3cPBRTraps_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,113,1,2,2))
_H3cPBRTrapsPrefix_ObjectIdentity=ObjectIdentity
h3cPBRTrapsPrefix=_H3cPBRTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,113,1,2,2,0))
h3cPBRNexthopFailedTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,113,1,2,2,0,1))
h3cPBRNexthopFailedTrap.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:h3cPBRNexthopFailedTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cPBR':h3cPBR,'h3cPBRObjects':h3cPBRObjects,'h3cPBRGlobal':h3cPBRGlobal,'h3cPBRNexthopTrapEnabled':h3cPBRNexthopTrapEnabled,'h3cPBRMibTrap':h3cPBRMibTrap,'h3cPBRTrapObjects':h3cPBRTrapObjects,_E:h3cPBRNexthopAddrType,_F:h3cPBRNexthopAddr,'h3cPBRTraps':h3cPBRTraps,'h3cPBRTrapsPrefix':h3cPBRTrapsPrefix,'h3cPBRNexthopFailedTrap':h3cPBRNexthopFailedTrap})