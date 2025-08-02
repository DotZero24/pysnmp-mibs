_M='not-accessible'
_L='hpnicfDLDPNeighborPortIndex'
_K='hpnicfDLDPNeighborBridgeMac'
_J='EnabledStatus'
_I='unknown'
_H='OctetString'
_G='HPN-ICF-DLDP-MIB'
_F='read-only'
_E='ifIndex'
_D='IF-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
hpnicfDldp=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,43))
if mibBuilder.loadTexts:hpnicfDldp.setRevisions(('2004-12-13 00:00',))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
class DLDPStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('initial',1),('inactive',2),('active',3),('advertisement',4),('probe',5),('disable',6)))
class DLDPNeighborStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unidirection',1),('bidirection',2),(_I,3)))
_HpnicfDLDPMibObject_ObjectIdentity=ObjectIdentity
hpnicfDLDPMibObject=_HpnicfDLDPMibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,43,1))
_HpnicfDLDPConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfDLDPConfigGroup=_HpnicfDLDPConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,43,1,1))
class _HpnicfDLDPWorkMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('enhance',2)))
_HpnicfDLDPWorkMode_Type.__name__=_C
_HpnicfDLDPWorkMode_Object=MibScalar
hpnicfDLDPWorkMode=_HpnicfDLDPWorkMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,1,1),_HpnicfDLDPWorkMode_Type())
hpnicfDLDPWorkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDLDPWorkMode.setStatus(_A)
_HpnicfDLDPSystemEnable_Type=TruthValue
_HpnicfDLDPSystemEnable_Object=MibScalar
hpnicfDLDPSystemEnable=_HpnicfDLDPSystemEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,1,2),_HpnicfDLDPSystemEnable_Type())
hpnicfDLDPSystemEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDLDPSystemEnable.setStatus(_A)
_HpnicfDLDPSystemReset_Type=TruthValue
_HpnicfDLDPSystemReset_Object=MibScalar
hpnicfDLDPSystemReset=_HpnicfDLDPSystemReset_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,1,3),_HpnicfDLDPSystemReset_Type())
hpnicfDLDPSystemReset.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDLDPSystemReset.setStatus(_A)
class _HpnicfDLDPInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfDLDPInterval_Type.__name__=_C
_HpnicfDLDPInterval_Object=MibScalar
hpnicfDLDPInterval=_HpnicfDLDPInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,1,4),_HpnicfDLDPInterval_Type())
hpnicfDLDPInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDLDPInterval.setStatus(_A)
class _HpnicfDLDPAuthenticationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('simple',2),('md5',3)))
_HpnicfDLDPAuthenticationMode_Type.__name__=_C
_HpnicfDLDPAuthenticationMode_Object=MibScalar
hpnicfDLDPAuthenticationMode=_HpnicfDLDPAuthenticationMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,1,5),_HpnicfDLDPAuthenticationMode_Type())
hpnicfDLDPAuthenticationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDLDPAuthenticationMode.setStatus(_A)
class _HpnicfDLDPAuthenticationPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,53))
_HpnicfDLDPAuthenticationPassword_Type.__name__=_H
_HpnicfDLDPAuthenticationPassword_Object=MibScalar
hpnicfDLDPAuthenticationPassword=_HpnicfDLDPAuthenticationPassword_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,1,6),_HpnicfDLDPAuthenticationPassword_Type())
hpnicfDLDPAuthenticationPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDLDPAuthenticationPassword.setStatus(_A)
class _HpnicfDLDPUnidirectionalShutdown_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manual',2)))
_HpnicfDLDPUnidirectionalShutdown_Type.__name__=_C
_HpnicfDLDPUnidirectionalShutdown_Object=MibScalar
hpnicfDLDPUnidirectionalShutdown=_HpnicfDLDPUnidirectionalShutdown_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,1,7),_HpnicfDLDPUnidirectionalShutdown_Type())
hpnicfDLDPUnidirectionalShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDLDPUnidirectionalShutdown.setStatus(_A)
_HpnicfDLDPPortStateTable_Object=MibTable
hpnicfDLDPPortStateTable=_HpnicfDLDPPortStateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,2))
if mibBuilder.loadTexts:hpnicfDLDPPortStateTable.setStatus(_A)
_HpnicfDLDPPortStateEntry_Object=MibTableRow
hpnicfDLDPPortStateEntry=_HpnicfDLDPPortStateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,2,1))
hpnicfDLDPPortStateEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfDLDPPortStateEntry.setStatus(_A)
class _HpnicfDLDPPortState_Type(EnabledStatus):defaultValue=2
_HpnicfDLDPPortState_Type.__name__=_J
_HpnicfDLDPPortState_Object=MibTableColumn
hpnicfDLDPPortState=_HpnicfDLDPPortState_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,2,1,1),_HpnicfDLDPPortState_Type())
hpnicfDLDPPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDLDPPortState.setStatus(_A)
_HpnicfDLDPPortDLDPTable_Object=MibTable
hpnicfDLDPPortDLDPTable=_HpnicfDLDPPortDLDPTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,3))
if mibBuilder.loadTexts:hpnicfDLDPPortDLDPTable.setStatus(_A)
_HpnicfDLDPPortDLDPEntry_Object=MibTableRow
hpnicfDLDPPortDLDPEntry=_HpnicfDLDPPortDLDPEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,3,1))
hpnicfDLDPPortDLDPEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfDLDPPortDLDPEntry.setStatus(_A)
_HpnicfDLDPPortDLDPState_Type=DLDPStatus
_HpnicfDLDPPortDLDPState_Object=MibTableColumn
hpnicfDLDPPortDLDPState=_HpnicfDLDPPortDLDPState_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,3,1,1),_HpnicfDLDPPortDLDPState_Type())
hpnicfDLDPPortDLDPState.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDLDPPortDLDPState.setStatus(_A)
class _HpnicfDLDPLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('up',2),(_I,3)))
_HpnicfDLDPLinkState_Type.__name__=_C
_HpnicfDLDPLinkState_Object=MibTableColumn
hpnicfDLDPLinkState=_HpnicfDLDPLinkState_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,3,1,2),_HpnicfDLDPLinkState_Type())
hpnicfDLDPLinkState.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDLDPLinkState.setStatus(_A)
_HpnicfDLDPPortDLDPReset_Type=TruthValue
_HpnicfDLDPPortDLDPReset_Object=MibTableColumn
hpnicfDLDPPortDLDPReset=_HpnicfDLDPPortDLDPReset_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,3,1,3),_HpnicfDLDPPortDLDPReset_Type())
hpnicfDLDPPortDLDPReset.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDLDPPortDLDPReset.setStatus(_A)
_HpnicfDLDPNeighborTable_Object=MibTable
hpnicfDLDPNeighborTable=_HpnicfDLDPNeighborTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,4))
if mibBuilder.loadTexts:hpnicfDLDPNeighborTable.setStatus(_A)
_HpnicfDLDPNeighborEntry_Object=MibTableRow
hpnicfDLDPNeighborEntry=_HpnicfDLDPNeighborEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,4,1))
hpnicfDLDPNeighborEntry.setIndexNames((0,_D,_E),(0,_G,_K),(0,_G,_L))
if mibBuilder.loadTexts:hpnicfDLDPNeighborEntry.setStatus(_A)
_HpnicfDLDPNeighborBridgeMac_Type=MacAddress
_HpnicfDLDPNeighborBridgeMac_Object=MibTableColumn
hpnicfDLDPNeighborBridgeMac=_HpnicfDLDPNeighborBridgeMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,4,1,1),_HpnicfDLDPNeighborBridgeMac_Type())
hpnicfDLDPNeighborBridgeMac.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfDLDPNeighborBridgeMac.setStatus(_A)
_HpnicfDLDPNeighborPortIndex_Type=Integer32
_HpnicfDLDPNeighborPortIndex_Object=MibTableColumn
hpnicfDLDPNeighborPortIndex=_HpnicfDLDPNeighborPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,4,1,2),_HpnicfDLDPNeighborPortIndex_Type())
hpnicfDLDPNeighborPortIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfDLDPNeighborPortIndex.setStatus(_A)
_HpnicfDLDPNeighborState_Type=DLDPNeighborStatus
_HpnicfDLDPNeighborState_Object=MibTableColumn
hpnicfDLDPNeighborState=_HpnicfDLDPNeighborState_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,4,1,3),_HpnicfDLDPNeighborState_Type())
hpnicfDLDPNeighborState.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDLDPNeighborState.setStatus(_A)
_HpnicfDLDPNeighborAgingTime_Type=Integer32
_HpnicfDLDPNeighborAgingTime_Object=MibTableColumn
hpnicfDLDPNeighborAgingTime=_HpnicfDLDPNeighborAgingTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,43,1,4,1,4),_HpnicfDLDPNeighborAgingTime_Type())
hpnicfDLDPNeighborAgingTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDLDPNeighborAgingTime.setStatus(_A)
_HpnicfDLDPTrapObject_ObjectIdentity=ObjectIdentity
hpnicfDLDPTrapObject=_HpnicfDLDPTrapObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,43,2))
_HpnicfDLDPNotification_ObjectIdentity=ObjectIdentity
hpnicfDLDPNotification=_HpnicfDLDPNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,43,2,1))
hpnicfDLDPUnidirectionalPort=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,43,2,1,1))
hpnicfDLDPUnidirectionalPort.setObjects((_D,_E))
if mibBuilder.loadTexts:hpnicfDLDPUnidirectionalPort.setStatus(_A)
mibBuilder.exportSymbols(_G,**{_J:EnabledStatus,'DLDPStatus':DLDPStatus,'DLDPNeighborStatus':DLDPNeighborStatus,'hpnicfDldp':hpnicfDldp,'hpnicfDLDPMibObject':hpnicfDLDPMibObject,'hpnicfDLDPConfigGroup':hpnicfDLDPConfigGroup,'hpnicfDLDPWorkMode':hpnicfDLDPWorkMode,'hpnicfDLDPSystemEnable':hpnicfDLDPSystemEnable,'hpnicfDLDPSystemReset':hpnicfDLDPSystemReset,'hpnicfDLDPInterval':hpnicfDLDPInterval,'hpnicfDLDPAuthenticationMode':hpnicfDLDPAuthenticationMode,'hpnicfDLDPAuthenticationPassword':hpnicfDLDPAuthenticationPassword,'hpnicfDLDPUnidirectionalShutdown':hpnicfDLDPUnidirectionalShutdown,'hpnicfDLDPPortStateTable':hpnicfDLDPPortStateTable,'hpnicfDLDPPortStateEntry':hpnicfDLDPPortStateEntry,'hpnicfDLDPPortState':hpnicfDLDPPortState,'hpnicfDLDPPortDLDPTable':hpnicfDLDPPortDLDPTable,'hpnicfDLDPPortDLDPEntry':hpnicfDLDPPortDLDPEntry,'hpnicfDLDPPortDLDPState':hpnicfDLDPPortDLDPState,'hpnicfDLDPLinkState':hpnicfDLDPLinkState,'hpnicfDLDPPortDLDPReset':hpnicfDLDPPortDLDPReset,'hpnicfDLDPNeighborTable':hpnicfDLDPNeighborTable,'hpnicfDLDPNeighborEntry':hpnicfDLDPNeighborEntry,_K:hpnicfDLDPNeighborBridgeMac,_L:hpnicfDLDPNeighborPortIndex,'hpnicfDLDPNeighborState':hpnicfDLDPNeighborState,'hpnicfDLDPNeighborAgingTime':hpnicfDLDPNeighborAgingTime,'hpnicfDLDPTrapObject':hpnicfDLDPTrapObject,'hpnicfDLDPNotification':hpnicfDLDPNotification,'hpnicfDLDPUnidirectionalPort':hpnicfDLDPUnidirectionalPort})