_i='ciscoEtherCfmMIBNotifGroup'
_h='ciscoEtherCfmMIBEventGroup'
_g='cEtherCfmXCheckServiceUp'
_f='cEtherCfmXCheckUnknown'
_e='cEtherCfmXCheckMissing'
_d='cEtherCfmCcConfigError'
_c='cEtherCfmCcLoop'
_b='cEtherCfmCcCrossconnect'
_a='cEtherCfmCcMepDown'
_Z='cEtherCfmCcMepUp'
_Y='cEtherCfmEventDeleteRow'
_X='cEtherCfmEventLastChange'
_W='cEtherCfmEventType'
_V='cEtherCfmEventDomainName'
_U='cEtherCfmMaxEventIndex'
_T='cEtherCfmEventIndex'
_S='cEtherCfmEventSvlan'
_R='cEtherCfmEventDomainIndex'
_Q='cEtherCfmEventRmtServiceId'
_P='cEtherCfmEventRmtPortState'
_O='not-accessible'
_N='SnmpAdminString'
_M='cEtherCfmEventCode'
_L='cEtherCfmEventLclIfCount'
_K='cEtherCfmEventLclMepCount'
_J='cEtherCfmEventLclMepid'
_I='Unsigned32'
_H='Integer32'
_G='cEtherCfmEventRmtMepid'
_F='cEtherCfmEventRmtMacAddress'
_E='cEtherCfmEventLclMacAddress'
_D='cEtherCfmEventServiceId'
_C='read-only'
_B='current'
_A='CISCO-ETHER-CFM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp')
ciscoEtherCfmMIB=ModuleIdentity((1,3,6,1,4,1,9,9,461))
if mibBuilder.loadTexts:ciscoEtherCfmMIB.setRevisions(('2004-12-28 00:00',))
class CfmMepid(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_CiscoEtherCfmMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoEtherCfmMIBNotifs=_CiscoEtherCfmMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,461,0))
_CiscoEtherCfmNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoEtherCfmNotificationPrefix=_CiscoEtherCfmNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,461,0,0))
_CiscoEtherCfmMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEtherCfmMIBObjects=_CiscoEtherCfmMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,461,1))
_CecCfmEvents_ObjectIdentity=ObjectIdentity
cecCfmEvents=_CecCfmEvents_ObjectIdentity((1,3,6,1,4,1,9,9,461,1,1))
class _CEtherCfmMaxEventIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CEtherCfmMaxEventIndex_Type.__name__=_I
_CEtherCfmMaxEventIndex_Object=MibScalar
cEtherCfmMaxEventIndex=_CEtherCfmMaxEventIndex_Object((1,3,6,1,4,1,9,9,461,1,1,1),_CEtherCfmMaxEventIndex_Type())
cEtherCfmMaxEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmMaxEventIndex.setStatus(_B)
_CEtherCfmEventTable_Object=MibTable
cEtherCfmEventTable=_CEtherCfmEventTable_Object((1,3,6,1,4,1,9,9,461,1,1,2))
if mibBuilder.loadTexts:cEtherCfmEventTable.setStatus(_B)
_CEtherCfmEventEntry_Object=MibTableRow
cEtherCfmEventEntry=_CEtherCfmEventEntry_Object((1,3,6,1,4,1,9,9,461,1,1,2,1))
cEtherCfmEventEntry.setIndexNames((0,_A,_R),(0,_A,_S),(0,_A,_T))
if mibBuilder.loadTexts:cEtherCfmEventEntry.setStatus(_B)
class _CEtherCfmEventDomainIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CEtherCfmEventDomainIndex_Type.__name__=_I
_CEtherCfmEventDomainIndex_Object=MibTableColumn
cEtherCfmEventDomainIndex=_CEtherCfmEventDomainIndex_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,1),_CEtherCfmEventDomainIndex_Type())
cEtherCfmEventDomainIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:cEtherCfmEventDomainIndex.setStatus(_B)
_CEtherCfmEventSvlan_Type=VlanId
_CEtherCfmEventSvlan_Object=MibTableColumn
cEtherCfmEventSvlan=_CEtherCfmEventSvlan_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,2),_CEtherCfmEventSvlan_Type())
cEtherCfmEventSvlan.setMaxAccess(_O)
if mibBuilder.loadTexts:cEtherCfmEventSvlan.setStatus(_B)
class _CEtherCfmEventIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CEtherCfmEventIndex_Type.__name__=_I
_CEtherCfmEventIndex_Object=MibTableColumn
cEtherCfmEventIndex=_CEtherCfmEventIndex_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,3),_CEtherCfmEventIndex_Type())
cEtherCfmEventIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:cEtherCfmEventIndex.setStatus(_B)
_CEtherCfmEventDomainName_Type=SnmpAdminString
_CEtherCfmEventDomainName_Object=MibTableColumn
cEtherCfmEventDomainName=_CEtherCfmEventDomainName_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,4),_CEtherCfmEventDomainName_Type())
cEtherCfmEventDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmEventDomainName.setStatus(_B)
class _CEtherCfmEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('mepUp',1),('mepDown',2),('xconnect',3),('loop',4),('config',5),('xcheckMissing',6),('xcheckUnknown',7),('xcheckServiceUp',8)))
_CEtherCfmEventType_Type.__name__=_H
_CEtherCfmEventType_Object=MibTableColumn
cEtherCfmEventType=_CEtherCfmEventType_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,5),_CEtherCfmEventType_Type())
cEtherCfmEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmEventType.setStatus(_B)
_CEtherCfmEventLastChange_Type=TimeStamp
_CEtherCfmEventLastChange_Object=MibTableColumn
cEtherCfmEventLastChange=_CEtherCfmEventLastChange_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,6),_CEtherCfmEventLastChange_Type())
cEtherCfmEventLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmEventLastChange.setStatus(_B)
class _CEtherCfmEventServiceId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CEtherCfmEventServiceId_Type.__name__=_N
_CEtherCfmEventServiceId_Object=MibTableColumn
cEtherCfmEventServiceId=_CEtherCfmEventServiceId_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,7),_CEtherCfmEventServiceId_Type())
cEtherCfmEventServiceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmEventServiceId.setStatus(_B)
_CEtherCfmEventLclMepid_Type=CfmMepid
_CEtherCfmEventLclMepid_Object=MibTableColumn
cEtherCfmEventLclMepid=_CEtherCfmEventLclMepid_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,8),_CEtherCfmEventLclMepid_Type())
cEtherCfmEventLclMepid.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmEventLclMepid.setStatus(_B)
_CEtherCfmEventLclMacAddress_Type=MacAddress
_CEtherCfmEventLclMacAddress_Object=MibTableColumn
cEtherCfmEventLclMacAddress=_CEtherCfmEventLclMacAddress_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,9),_CEtherCfmEventLclMacAddress_Type())
cEtherCfmEventLclMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmEventLclMacAddress.setStatus(_B)
_CEtherCfmEventLclMepCount_Type=Gauge32
_CEtherCfmEventLclMepCount_Object=MibTableColumn
cEtherCfmEventLclMepCount=_CEtherCfmEventLclMepCount_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,10),_CEtherCfmEventLclMepCount_Type())
cEtherCfmEventLclMepCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmEventLclMepCount.setStatus(_B)
_CEtherCfmEventLclIfCount_Type=Gauge32
_CEtherCfmEventLclIfCount_Object=MibTableColumn
cEtherCfmEventLclIfCount=_CEtherCfmEventLclIfCount_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,11),_CEtherCfmEventLclIfCount_Type())
cEtherCfmEventLclIfCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmEventLclIfCount.setStatus(_B)
_CEtherCfmEventRmtMepid_Type=CfmMepid
_CEtherCfmEventRmtMepid_Object=MibTableColumn
cEtherCfmEventRmtMepid=_CEtherCfmEventRmtMepid_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,12),_CEtherCfmEventRmtMepid_Type())
cEtherCfmEventRmtMepid.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmEventRmtMepid.setStatus(_B)
_CEtherCfmEventRmtMacAddress_Type=MacAddress
_CEtherCfmEventRmtMacAddress_Object=MibTableColumn
cEtherCfmEventRmtMacAddress=_CEtherCfmEventRmtMacAddress_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,13),_CEtherCfmEventRmtMacAddress_Type())
cEtherCfmEventRmtMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmEventRmtMacAddress.setStatus(_B)
class _CEtherCfmEventRmtPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),('adminDown',3),('test',4),('remoteExcessiveErrors',5),('localExcessiveErrors',6),('localNoData',7)))
_CEtherCfmEventRmtPortState_Type.__name__=_H
_CEtherCfmEventRmtPortState_Object=MibTableColumn
cEtherCfmEventRmtPortState=_CEtherCfmEventRmtPortState_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,14),_CEtherCfmEventRmtPortState_Type())
cEtherCfmEventRmtPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmEventRmtPortState.setStatus(_B)
class _CEtherCfmEventRmtServiceId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CEtherCfmEventRmtServiceId_Type.__name__=_N
_CEtherCfmEventRmtServiceId_Object=MibTableColumn
cEtherCfmEventRmtServiceId=_CEtherCfmEventRmtServiceId_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,15),_CEtherCfmEventRmtServiceId_Type())
cEtherCfmEventRmtServiceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmEventRmtServiceId.setStatus(_B)
class _CEtherCfmEventCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('new',1),('returning',2),('portState',3),('lastGasp',4),('timeout',5),('configClear',6),('loopClear',7),('xconnectClear',8),('unknownClear',9)))
_CEtherCfmEventCode_Type.__name__=_H
_CEtherCfmEventCode_Object=MibTableColumn
cEtherCfmEventCode=_CEtherCfmEventCode_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,16),_CEtherCfmEventCode_Type())
cEtherCfmEventCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cEtherCfmEventCode.setStatus(_B)
class _CEtherCfmEventDeleteRow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noop',1),('delete',2)))
_CEtherCfmEventDeleteRow_Type.__name__=_H
_CEtherCfmEventDeleteRow_Object=MibTableColumn
cEtherCfmEventDeleteRow=_CEtherCfmEventDeleteRow_Object((1,3,6,1,4,1,9,9,461,1,1,2,1,17),_CEtherCfmEventDeleteRow_Type())
cEtherCfmEventDeleteRow.setMaxAccess('read-write')
if mibBuilder.loadTexts:cEtherCfmEventDeleteRow.setStatus(_B)
_CiscoEtherCfmMIBConform_ObjectIdentity=ObjectIdentity
ciscoEtherCfmMIBConform=_CiscoEtherCfmMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,461,2))
_CiscoEtherCfmMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoEtherCfmMIBCompliances=_CiscoEtherCfmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,461,2,1))
_CiscoEtherCfmMIBGroups_ObjectIdentity=ObjectIdentity
ciscoEtherCfmMIBGroups=_CiscoEtherCfmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,461,2,2))
ciscoEtherCfmMIBEventGroup=ObjectGroup((1,3,6,1,4,1,9,9,461,2,2,1))
ciscoEtherCfmMIBEventGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_D),(_A,_J),(_A,_E),(_A,_K),(_A,_L),(_A,_G),(_A,_F),(_A,_P),(_A,_Q),(_A,_M),(_A,_Y)))
if mibBuilder.loadTexts:ciscoEtherCfmMIBEventGroup.setStatus(_B)
cEtherCfmCcMepUp=NotificationType((1,3,6,1,4,1,9,9,461,0,0,1))
cEtherCfmCcMepUp.setObjects(*((_A,_D),(_A,_E),(_A,_K),(_A,_L),(_A,_G),(_A,_F),(_A,_M),(_A,_P)))
if mibBuilder.loadTexts:cEtherCfmCcMepUp.setStatus(_B)
cEtherCfmCcMepDown=NotificationType((1,3,6,1,4,1,9,9,461,0,0,2))
cEtherCfmCcMepDown.setObjects(*((_A,_D),(_A,_E),(_A,_K),(_A,_L),(_A,_G),(_A,_F),(_A,_M)))
if mibBuilder.loadTexts:cEtherCfmCcMepDown.setStatus(_B)
cEtherCfmCcCrossconnect=NotificationType((1,3,6,1,4,1,9,9,461,0,0,3))
cEtherCfmCcCrossconnect.setObjects(*((_A,_D),(_A,_E),(_A,_G),(_A,_F),(_A,_Q)))
if mibBuilder.loadTexts:cEtherCfmCcCrossconnect.setStatus(_B)
cEtherCfmCcLoop=NotificationType((1,3,6,1,4,1,9,9,461,0,0,4))
cEtherCfmCcLoop.setObjects(*((_A,_D),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:cEtherCfmCcLoop.setStatus(_B)
cEtherCfmCcConfigError=NotificationType((1,3,6,1,4,1,9,9,461,0,0,5))
cEtherCfmCcConfigError.setObjects(*((_A,_D),(_A,_E),(_A,_J),(_A,_F)))
if mibBuilder.loadTexts:cEtherCfmCcConfigError.setStatus(_B)
cEtherCfmXCheckMissing=NotificationType((1,3,6,1,4,1,9,9,461,0,0,6))
cEtherCfmXCheckMissing.setObjects(*((_A,_D),(_A,_E),(_A,_G),(_A,_F)))
if mibBuilder.loadTexts:cEtherCfmXCheckMissing.setStatus(_B)
cEtherCfmXCheckUnknown=NotificationType((1,3,6,1,4,1,9,9,461,0,0,7))
cEtherCfmXCheckUnknown.setObjects(*((_A,_D),(_A,_E),(_A,_G),(_A,_F)))
if mibBuilder.loadTexts:cEtherCfmXCheckUnknown.setStatus(_B)
cEtherCfmXCheckServiceUp=NotificationType((1,3,6,1,4,1,9,9,461,0,0,8))
cEtherCfmXCheckServiceUp.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:cEtherCfmXCheckServiceUp.setStatus(_B)
ciscoEtherCfmMIBNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,461,2,2,2))
ciscoEtherCfmMIBNotifGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ciscoEtherCfmMIBNotifGroup.setStatus(_B)
ciscoEtherCfmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,461,2,1,1))
ciscoEtherCfmMIBCompliance.setObjects(*((_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ciscoEtherCfmMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CfmMepid':CfmMepid,'ciscoEtherCfmMIB':ciscoEtherCfmMIB,'ciscoEtherCfmMIBNotifs':ciscoEtherCfmMIBNotifs,'ciscoEtherCfmNotificationPrefix':ciscoEtherCfmNotificationPrefix,_Z:cEtherCfmCcMepUp,_a:cEtherCfmCcMepDown,_b:cEtherCfmCcCrossconnect,_c:cEtherCfmCcLoop,_d:cEtherCfmCcConfigError,_e:cEtherCfmXCheckMissing,_f:cEtherCfmXCheckUnknown,_g:cEtherCfmXCheckServiceUp,'ciscoEtherCfmMIBObjects':ciscoEtherCfmMIBObjects,'cecCfmEvents':cecCfmEvents,_U:cEtherCfmMaxEventIndex,'cEtherCfmEventTable':cEtherCfmEventTable,'cEtherCfmEventEntry':cEtherCfmEventEntry,_R:cEtherCfmEventDomainIndex,_S:cEtherCfmEventSvlan,_T:cEtherCfmEventIndex,_V:cEtherCfmEventDomainName,_W:cEtherCfmEventType,_X:cEtherCfmEventLastChange,_D:cEtherCfmEventServiceId,_J:cEtherCfmEventLclMepid,_E:cEtherCfmEventLclMacAddress,_K:cEtherCfmEventLclMepCount,_L:cEtherCfmEventLclIfCount,_G:cEtherCfmEventRmtMepid,_F:cEtherCfmEventRmtMacAddress,_P:cEtherCfmEventRmtPortState,_Q:cEtherCfmEventRmtServiceId,_M:cEtherCfmEventCode,_Y:cEtherCfmEventDeleteRow,'ciscoEtherCfmMIBConform':ciscoEtherCfmMIBConform,'ciscoEtherCfmMIBCompliances':ciscoEtherCfmMIBCompliances,'ciscoEtherCfmMIBCompliance':ciscoEtherCfmMIBCompliance,'ciscoEtherCfmMIBGroups':ciscoEtherCfmMIBGroups,_h:ciscoEtherCfmMIBEventGroup,_i:ciscoEtherCfmMIBNotifGroup})