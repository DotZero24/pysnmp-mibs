_N='interfaceName'
_M='networkAddress'
_L='macAddress'
_K='portComponent'
_J='interfaceAlias'
_I='ifIndex'
_H='IF-MIB'
_G='eqlMemberIndex'
_F='EQLMEMBER-MIB'
_E='eqlGroupId'
_D='EQLGROUP-MIB'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eqlGroupId,=mibBuilder.importSymbols(_D,_E)
eqlMemberIndex,=mibBuilder.importSymbols(_F,_G)
equalLogic,=mibBuilder.importSymbols('EQUALLOGIC-SMI','equalLogic')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeInterval','TruthValue')
eqlLldpMib=ModuleIdentity((1,3,6,1,4,1,12740,21))
if mibBuilder.loadTexts:eqlLldpMib.setRevisions(('2010-07-23 00:00',))
class EqlLldpV2ChassisIdSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('chassisComponent',1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),('local',7)))
class EqlLldpV2ChassisId(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
class EqlLldpV2PortIdSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),('agentCircuitId',6),('local',7)))
class EqlLldpV2PortId(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class EqlLldpV2State(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('off',0),('noPeer',1),('active',2),('multiplePeers',3)))
_EqlLldpMIBObjects_ObjectIdentity=ObjectIdentity
eqlLldpMIBObjects=_EqlLldpMIBObjects_ObjectIdentity((1,3,6,1,4,1,12740,21,1))
_EqlLldpDynamicIfTable_Object=MibTable
eqlLldpDynamicIfTable=_EqlLldpDynamicIfTable_Object((1,3,6,1,4,1,12740,21,1,1))
if mibBuilder.loadTexts:eqlLldpDynamicIfTable.setStatus(_A)
_EqlLldpDynamicIfEntry_Object=MibTableRow
eqlLldpDynamicIfEntry=_EqlLldpDynamicIfEntry_Object((1,3,6,1,4,1,12740,21,1,1,1))
eqlLldpDynamicIfEntry.setIndexNames((0,_D,_E),(0,_F,_G),(0,_H,_I))
if mibBuilder.loadTexts:eqlLldpDynamicIfEntry.setStatus(_A)
_EqlLldpRemMacAddress_Type=MacAddress
_EqlLldpRemMacAddress_Object=MibTableColumn
eqlLldpRemMacAddress=_EqlLldpRemMacAddress_Object((1,3,6,1,4,1,12740,21,1,1,1,1),_EqlLldpRemMacAddress_Type())
eqlLldpRemMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlLldpRemMacAddress.setStatus(_A)
_EqlLldpV2RemChassisIdSubtype_Type=EqlLldpV2ChassisIdSubtype
_EqlLldpV2RemChassisIdSubtype_Object=MibTableColumn
eqlLldpV2RemChassisIdSubtype=_EqlLldpV2RemChassisIdSubtype_Object((1,3,6,1,4,1,12740,21,1,1,1,2),_EqlLldpV2RemChassisIdSubtype_Type())
eqlLldpV2RemChassisIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlLldpV2RemChassisIdSubtype.setStatus(_A)
_EqlLldpV2RemChassisId_Type=EqlLldpV2ChassisId
_EqlLldpV2RemChassisId_Object=MibTableColumn
eqlLldpV2RemChassisId=_EqlLldpV2RemChassisId_Object((1,3,6,1,4,1,12740,21,1,1,1,3),_EqlLldpV2RemChassisId_Type())
eqlLldpV2RemChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlLldpV2RemChassisId.setStatus(_A)
_EqlLldpV2RemPortIdSubtype_Type=EqlLldpV2PortIdSubtype
_EqlLldpV2RemPortIdSubtype_Object=MibTableColumn
eqlLldpV2RemPortIdSubtype=_EqlLldpV2RemPortIdSubtype_Object((1,3,6,1,4,1,12740,21,1,1,1,4),_EqlLldpV2RemPortIdSubtype_Type())
eqlLldpV2RemPortIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlLldpV2RemPortIdSubtype.setStatus(_A)
_EqlLldpV2RemPortId_Type=EqlLldpV2PortId
_EqlLldpV2RemPortId_Object=MibTableColumn
eqlLldpV2RemPortId=_EqlLldpV2RemPortId_Object((1,3,6,1,4,1,12740,21,1,1,1,5),_EqlLldpV2RemPortId_Type())
eqlLldpV2RemPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlLldpV2RemPortId.setStatus(_A)
class _EqlLldpV2RemPortDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EqlLldpV2RemPortDesc_Type.__name__=_C
_EqlLldpV2RemPortDesc_Object=MibTableColumn
eqlLldpV2RemPortDesc=_EqlLldpV2RemPortDesc_Object((1,3,6,1,4,1,12740,21,1,1,1,6),_EqlLldpV2RemPortDesc_Type())
eqlLldpV2RemPortDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlLldpV2RemPortDesc.setStatus(_A)
class _EqlLldpV2RemSysName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EqlLldpV2RemSysName_Type.__name__=_C
_EqlLldpV2RemSysName_Object=MibTableColumn
eqlLldpV2RemSysName=_EqlLldpV2RemSysName_Object((1,3,6,1,4,1,12740,21,1,1,1,7),_EqlLldpV2RemSysName_Type())
eqlLldpV2RemSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlLldpV2RemSysName.setStatus(_A)
class _EqlLldpV2RemSysDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EqlLldpV2RemSysDesc_Type.__name__=_C
_EqlLldpV2RemSysDesc_Object=MibTableColumn
eqlLldpV2RemSysDesc=_EqlLldpV2RemSysDesc_Object((1,3,6,1,4,1,12740,21,1,1,1,8),_EqlLldpV2RemSysDesc_Type())
eqlLldpV2RemSysDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlLldpV2RemSysDesc.setStatus(_A)
_EqlLldpV2State_Type=EqlLldpV2State
_EqlLldpV2State_Object=MibTableColumn
eqlLldpV2State=_EqlLldpV2State_Object((1,3,6,1,4,1,12740,21,1,1,1,9),_EqlLldpV2State_Type())
eqlLldpV2State.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlLldpV2State.setStatus(_A)
class _EqlLldpV2RemMgmtAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EqlLldpV2RemMgmtAddr_Type.__name__=_C
_EqlLldpV2RemMgmtAddr_Object=MibTableColumn
eqlLldpV2RemMgmtAddr=_EqlLldpV2RemMgmtAddr_Object((1,3,6,1,4,1,12740,21,1,1,1,10),_EqlLldpV2RemMgmtAddr_Type())
eqlLldpV2RemMgmtAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlLldpV2RemMgmtAddr.setStatus(_A)
mibBuilder.exportSymbols('EQL-LLDP-MIB',**{'EqlLldpV2ChassisIdSubtype':EqlLldpV2ChassisIdSubtype,'EqlLldpV2ChassisId':EqlLldpV2ChassisId,'EqlLldpV2PortIdSubtype':EqlLldpV2PortIdSubtype,'EqlLldpV2PortId':EqlLldpV2PortId,'EqlLldpV2State':EqlLldpV2State,'eqlLldpMib':eqlLldpMib,'eqlLldpMIBObjects':eqlLldpMIBObjects,'eqlLldpDynamicIfTable':eqlLldpDynamicIfTable,'eqlLldpDynamicIfEntry':eqlLldpDynamicIfEntry,'eqlLldpRemMacAddress':eqlLldpRemMacAddress,'eqlLldpV2RemChassisIdSubtype':eqlLldpV2RemChassisIdSubtype,'eqlLldpV2RemChassisId':eqlLldpV2RemChassisId,'eqlLldpV2RemPortIdSubtype':eqlLldpV2RemPortIdSubtype,'eqlLldpV2RemPortId':eqlLldpV2RemPortId,'eqlLldpV2RemPortDesc':eqlLldpV2RemPortDesc,'eqlLldpV2RemSysName':eqlLldpV2RemSysName,'eqlLldpV2RemSysDesc':eqlLldpV2RemSysDesc,'eqlLldpV2State':eqlLldpV2State,'eqlLldpV2RemMgmtAddr':eqlLldpV2RemMgmtAddr})