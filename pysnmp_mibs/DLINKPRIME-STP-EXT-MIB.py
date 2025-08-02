_K='dpStpExtMstpGroup'
_J='dpStpExtBasicGroup'
_I='dpStpExtPortFast'
_H='dpStpExtNotificationEnable'
_G='dpStpExtPortState'
_F='dpStpExtStpGblStateEnabled'
_E='dpStpExtPortNumber'
_D='read-write'
_C='Integer32'
_B='DLINKPRIME-STP-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
dlinkPrimeStpExtMIB=ModuleIdentity((1,3,6,1,4,1,171,15,18))
if mibBuilder.loadTexts:dlinkPrimeStpExtMIB.setRevisions(('2014-06-05 00:00',))
class IEEE8021BridgePortNumber(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DpStpExtMIBNotifications_ObjectIdentity=ObjectIdentity
dpStpExtMIBNotifications=_DpStpExtMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,18,0))
_DpStpExtMIBObjects_ObjectIdentity=ObjectIdentity
dpStpExtMIBObjects=_DpStpExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,18,1))
_DpStpExtGblMgmt_ObjectIdentity=ObjectIdentity
dpStpExtGblMgmt=_DpStpExtGblMgmt_ObjectIdentity((1,3,6,1,4,1,171,15,18,1,1))
_DpStpExtStpGblStateEnabled_Type=TruthValue
_DpStpExtStpGblStateEnabled_Object=MibScalar
dpStpExtStpGblStateEnabled=_DpStpExtStpGblStateEnabled_Object((1,3,6,1,4,1,171,15,18,1,1,1),_DpStpExtStpGblStateEnabled_Type())
dpStpExtStpGblStateEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:dpStpExtStpGblStateEnabled.setStatus(_A)
class _DpStpExtStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp',1),('rstp',2)))
_DpStpExtStpMode_Type.__name__=_C
_DpStpExtStpMode_Object=MibScalar
dpStpExtStpMode=_DpStpExtStpMode_Object((1,3,6,1,4,1,171,15,18,1,1,2),_DpStpExtStpMode_Type())
dpStpExtStpMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dpStpExtStpMode.setStatus(_A)
class _DpStpExtNotificationEnable_Type(Bits):namedValues=NamedValues(*(('newRoot',0),('topologyChange',1)))
_DpStpExtNotificationEnable_Type.__name__='Bits'
_DpStpExtNotificationEnable_Object=MibScalar
dpStpExtNotificationEnable=_DpStpExtNotificationEnable_Object((1,3,6,1,4,1,171,15,18,1,1,3),_DpStpExtNotificationEnable_Type())
dpStpExtNotificationEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dpStpExtNotificationEnable.setStatus(_A)
_DpStpExtPortMgmt_ObjectIdentity=ObjectIdentity
dpStpExtPortMgmt=_DpStpExtPortMgmt_ObjectIdentity((1,3,6,1,4,1,171,15,18,1,2))
_DpStpExtPortTable_Object=MibTable
dpStpExtPortTable=_DpStpExtPortTable_Object((1,3,6,1,4,1,171,15,18,1,2,1))
if mibBuilder.loadTexts:dpStpExtPortTable.setStatus(_A)
_DpStpExtPortEntry_Object=MibTableRow
dpStpExtPortEntry=_DpStpExtPortEntry_Object((1,3,6,1,4,1,171,15,18,1,2,1,1))
dpStpExtPortEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:dpStpExtPortEntry.setStatus(_A)
_DpStpExtPortNumber_Type=IEEE8021BridgePortNumber
_DpStpExtPortNumber_Object=MibTableColumn
dpStpExtPortNumber=_DpStpExtPortNumber_Object((1,3,6,1,4,1,171,15,18,1,2,1,1,1),_DpStpExtPortNumber_Type())
dpStpExtPortNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dpStpExtPortNumber.setStatus(_A)
class _DpStpExtPortFast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('network',1),('disabled',2),('edge',3)))
_DpStpExtPortFast_Type.__name__=_C
_DpStpExtPortFast_Object=MibTableColumn
dpStpExtPortFast=_DpStpExtPortFast_Object((1,3,6,1,4,1,171,15,18,1,2,1,1,2),_DpStpExtPortFast_Type())
dpStpExtPortFast.setMaxAccess(_D)
if mibBuilder.loadTexts:dpStpExtPortFast.setStatus(_A)
class _DpStpExtPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('errDisabled',1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6),('nonStpForwarding',7),('nonStpOther',8)))
_DpStpExtPortState_Type.__name__=_C
_DpStpExtPortState_Object=MibTableColumn
dpStpExtPortState=_DpStpExtPortState_Object((1,3,6,1,4,1,171,15,18,1,2,1,1,3),_DpStpExtPortState_Type())
dpStpExtPortState.setMaxAccess('read-only')
if mibBuilder.loadTexts:dpStpExtPortState.setStatus(_A)
_DpStpExtMIBConformance_ObjectIdentity=ObjectIdentity
dpStpExtMIBConformance=_DpStpExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,18,2))
_DpStpExtMIBCompliances_ObjectIdentity=ObjectIdentity
dpStpExtMIBCompliances=_DpStpExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,18,2,1))
_DpStpExtGroups_ObjectIdentity=ObjectIdentity
dpStpExtGroups=_DpStpExtGroups_ObjectIdentity((1,3,6,1,4,1,171,15,18,2,1,2))
dpStpExtBasicGroup=ObjectGroup((1,3,6,1,4,1,171,15,18,2,1,2,1))
dpStpExtBasicGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:dpStpExtBasicGroup.setStatus(_A)
dpStpExtMstpGroup=ObjectGroup((1,3,6,1,4,1,171,15,18,2,1,2,2))
dpStpExtMstpGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:dpStpExtMstpGroup.setStatus(_A)
dpStpExtCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,18,2,1,1))
dpStpExtCompliance.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:dpStpExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IEEE8021BridgePortNumber':IEEE8021BridgePortNumber,'dlinkPrimeStpExtMIB':dlinkPrimeStpExtMIB,'dpStpExtMIBNotifications':dpStpExtMIBNotifications,'dpStpExtMIBObjects':dpStpExtMIBObjects,'dpStpExtGblMgmt':dpStpExtGblMgmt,_F:dpStpExtStpGblStateEnabled,'dpStpExtStpMode':dpStpExtStpMode,_H:dpStpExtNotificationEnable,'dpStpExtPortMgmt':dpStpExtPortMgmt,'dpStpExtPortTable':dpStpExtPortTable,'dpStpExtPortEntry':dpStpExtPortEntry,_E:dpStpExtPortNumber,_I:dpStpExtPortFast,_G:dpStpExtPortState,'dpStpExtMIBConformance':dpStpExtMIBConformance,'dpStpExtMIBCompliances':dpStpExtMIBCompliances,'dpStpExtCompliance':dpStpExtCompliance,'dpStpExtGroups':dpStpExtGroups,_J:dpStpExtBasicGroup,_K:dpStpExtMstpGroup})