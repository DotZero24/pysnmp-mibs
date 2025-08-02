_P='h3cConStatusGroup'
_O='h3cUIMgtBasicGroup'
_N='h3cTerminalUserAuthFailureReason'
_M='h3cConReAuth'
_L='h3cVtyAccAclNum'
_K='h3cConUserIndex'
_J='read-create'
_I='h3cVtyAccConnway'
_H='h3cVtyAccUserIndex'
_G='not-accessible'
_F='accessible-for-notify'
_E='h3cTerminalSource'
_D='h3cTerminalUserName'
_C='Integer32'
_B='H3C-UI-MAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cUIMgt=ModuleIdentity((1,3,6,1,4,1,2011,10,2,2))
_H3cUIMgtObjects_ObjectIdentity=ObjectIdentity
h3cUIMgtObjects=_H3cUIMgtObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,2,1))
_H3cUIBasicInfo_ObjectIdentity=ObjectIdentity
h3cUIBasicInfo=_H3cUIBasicInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,2,1,1))
_H3cUIScalarObjects_ObjectIdentity=ObjectIdentity
h3cUIScalarObjects=_H3cUIScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,2,1,1,1))
_H3cUITrapBindObjects_ObjectIdentity=ObjectIdentity
h3cUITrapBindObjects=_H3cUITrapBindObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,2,1,1,2))
_H3cTerminalUserName_Type=DisplayString
_H3cTerminalUserName_Object=MibScalar
h3cTerminalUserName=_H3cTerminalUserName_Object((1,3,6,1,4,1,2011,10,2,2,1,1,2,1),_H3cTerminalUserName_Type())
h3cTerminalUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cTerminalUserName.setStatus(_A)
_H3cTerminalSource_Type=DisplayString
_H3cTerminalSource_Object=MibScalar
h3cTerminalSource=_H3cTerminalSource_Object((1,3,6,1,4,1,2011,10,2,2,1,1,2,2),_H3cTerminalSource_Type())
h3cTerminalSource.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cTerminalSource.setStatus(_A)
class _H3cTerminalUserAuthFailureReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('exceedRetries',1),('authTimeout',2),('otherReason',3)))
_H3cTerminalUserAuthFailureReason_Type.__name__=_C
_H3cTerminalUserAuthFailureReason_Object=MibScalar
h3cTerminalUserAuthFailureReason=_H3cTerminalUserAuthFailureReason_Object((1,3,6,1,4,1,2011,10,2,2,1,1,2,3),_H3cTerminalUserAuthFailureReason_Type())
h3cTerminalUserAuthFailureReason.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cTerminalUserAuthFailureReason.setStatus(_A)
_H3cUINotifications_ObjectIdentity=ObjectIdentity
h3cUINotifications=_H3cUINotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,2,1,1,3))
_H3cUINotificationsPrefix_ObjectIdentity=ObjectIdentity
h3cUINotificationsPrefix=_H3cUINotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,2,1,1,3,0))
_H3cVtyMan_ObjectIdentity=ObjectIdentity
h3cVtyMan=_H3cVtyMan_ObjectIdentity((1,3,6,1,4,1,2011,10,2,2,1,2))
_H3cVtyAccTable_Object=MibTable
h3cVtyAccTable=_H3cVtyAccTable_Object((1,3,6,1,4,1,2011,10,2,2,1,2,1))
if mibBuilder.loadTexts:h3cVtyAccTable.setStatus(_A)
_H3cVtyAccEntry_Object=MibTableRow
h3cVtyAccEntry=_H3cVtyAccEntry_Object((1,3,6,1,4,1,2011,10,2,2,1,2,1,1))
h3cVtyAccEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:h3cVtyAccEntry.setStatus(_A)
class _H3cVtyAccUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cVtyAccUserIndex_Type.__name__=_C
_H3cVtyAccUserIndex_Object=MibTableColumn
h3cVtyAccUserIndex=_H3cVtyAccUserIndex_Object((1,3,6,1,4,1,2011,10,2,2,1,2,1,1,1),_H3cVtyAccUserIndex_Type())
h3cVtyAccUserIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cVtyAccUserIndex.setStatus(_A)
class _H3cVtyAccConnway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,11,12)));namedValues=NamedValues(*(('inbound',1),('outbound',2),('linkinbound',3),('acl6inbound',11),('acl6outbound',12)))
_H3cVtyAccConnway_Type.__name__=_C
_H3cVtyAccConnway_Object=MibTableColumn
h3cVtyAccConnway=_H3cVtyAccConnway_Object((1,3,6,1,4,1,2011,10,2,2,1,2,1,1,2),_H3cVtyAccConnway_Type())
h3cVtyAccConnway.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cVtyAccConnway.setStatus(_A)
_H3cVtyAccAclNum_Type=Integer32
_H3cVtyAccAclNum_Object=MibTableColumn
h3cVtyAccAclNum=_H3cVtyAccAclNum_Object((1,3,6,1,4,1,2011,10,2,2,1,2,1,1,3),_H3cVtyAccAclNum_Type())
h3cVtyAccAclNum.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cVtyAccAclNum.setStatus(_A)
_H3cVtyAccEntryRowStatus_Type=RowStatus
_H3cVtyAccEntryRowStatus_Object=MibTableColumn
h3cVtyAccEntryRowStatus=_H3cVtyAccEntryRowStatus_Object((1,3,6,1,4,1,2011,10,2,2,1,2,1,1,4),_H3cVtyAccEntryRowStatus_Type())
h3cVtyAccEntryRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cVtyAccEntryRowStatus.setStatus(_A)
_H3cConStatus_ObjectIdentity=ObjectIdentity
h3cConStatus=_H3cConStatus_ObjectIdentity((1,3,6,1,4,1,2011,10,2,2,1,3))
_H3cConStatusTable_Object=MibTable
h3cConStatusTable=_H3cConStatusTable_Object((1,3,6,1,4,1,2011,10,2,2,1,3,1))
if mibBuilder.loadTexts:h3cConStatusTable.setStatus(_A)
_H3cConStatusEntry_Object=MibTableRow
h3cConStatusEntry=_H3cConStatusEntry_Object((1,3,6,1,4,1,2011,10,2,2,1,3,1,1))
h3cConStatusEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:h3cConStatusEntry.setStatus(_A)
_H3cConUserIndex_Type=Integer32
_H3cConUserIndex_Object=MibTableColumn
h3cConUserIndex=_H3cConUserIndex_Object((1,3,6,1,4,1,2011,10,2,2,1,3,1,1,1),_H3cConUserIndex_Type())
h3cConUserIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cConUserIndex.setStatus(_A)
class _H3cConReAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_H3cConReAuth_Type.__name__=_C
_H3cConReAuth_Object=MibTableColumn
h3cConReAuth=_H3cConReAuth_Object((1,3,6,1,4,1,2011,10,2,2,1,3,1,1,2),_H3cConReAuth_Type())
h3cConReAuth.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cConReAuth.setStatus(_A)
_H3cUIMgtMIBConformance18_ObjectIdentity=ObjectIdentity
h3cUIMgtMIBConformance18=_H3cUIMgtMIBConformance18_ObjectIdentity((1,3,6,1,4,1,2011,10,2,2,2))
_H3cUIMgtMIBCompliances_ObjectIdentity=ObjectIdentity
h3cUIMgtMIBCompliances=_H3cUIMgtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,2,2,1))
_H3cUIMgtManMIBGroups_ObjectIdentity=ObjectIdentity
h3cUIMgtManMIBGroups=_H3cUIMgtManMIBGroups_ObjectIdentity((1,3,6,1,4,1,2011,10,2,2,2,2))
h3cUIMgtBasicGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,2,2,2,1))
h3cUIMgtBasicGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:h3cUIMgtBasicGroup.setStatus(_A)
h3cConStatusGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,2,2,2,2))
h3cConStatusGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:h3cConStatusGroup.setStatus(_A)
h3cLogIn=NotificationType((1,3,6,1,4,1,2011,10,2,2,1,1,3,0,1))
h3cLogIn.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:h3cLogIn.setStatus(_A)
h3cLogOut=NotificationType((1,3,6,1,4,1,2011,10,2,2,1,1,3,0,2))
h3cLogOut.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:h3cLogOut.setStatus(_A)
h3cLogInAuthenFailure=NotificationType((1,3,6,1,4,1,2011,10,2,2,1,1,3,0,3))
h3cLogInAuthenFailure.setObjects(*((_B,_D),(_B,_E),(_B,_N)))
if mibBuilder.loadTexts:h3cLogInAuthenFailure.setStatus(_A)
h3cUIMgtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,2,2,1,1))
h3cUIMgtMIBCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:h3cUIMgtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cUIMgt':h3cUIMgt,'h3cUIMgtObjects':h3cUIMgtObjects,'h3cUIBasicInfo':h3cUIBasicInfo,'h3cUIScalarObjects':h3cUIScalarObjects,'h3cUITrapBindObjects':h3cUITrapBindObjects,_D:h3cTerminalUserName,_E:h3cTerminalSource,_N:h3cTerminalUserAuthFailureReason,'h3cUINotifications':h3cUINotifications,'h3cUINotificationsPrefix':h3cUINotificationsPrefix,'h3cLogIn':h3cLogIn,'h3cLogOut':h3cLogOut,'h3cLogInAuthenFailure':h3cLogInAuthenFailure,'h3cVtyMan':h3cVtyMan,'h3cVtyAccTable':h3cVtyAccTable,'h3cVtyAccEntry':h3cVtyAccEntry,_H:h3cVtyAccUserIndex,_I:h3cVtyAccConnway,_L:h3cVtyAccAclNum,'h3cVtyAccEntryRowStatus':h3cVtyAccEntryRowStatus,'h3cConStatus':h3cConStatus,'h3cConStatusTable':h3cConStatusTable,'h3cConStatusEntry':h3cConStatusEntry,_K:h3cConUserIndex,_M:h3cConReAuth,'h3cUIMgtMIBConformance18':h3cUIMgtMIBConformance18,'h3cUIMgtMIBCompliances':h3cUIMgtMIBCompliances,'h3cUIMgtMIBCompliance':h3cUIMgtMIBCompliance,'h3cUIMgtManMIBGroups':h3cUIMgtManMIBGroups,_O:h3cUIMgtBasicGroup,_P:h3cConStatusGroup})