_P='hpnicfConStatusGroup'
_O='hpnicfUIMgtBasicGroup'
_N='hpnicfTerminalUserAuthFailureReason'
_M='hpnicfConReAuth'
_L='hpnicfVtyAccAclNum'
_K='hpnicfConUserIndex'
_J='read-create'
_I='hpnicfVtyAccConnway'
_H='hpnicfVtyAccUserIndex'
_G='not-accessible'
_F='accessible-for-notify'
_E='hpnicfTerminalSource'
_D='hpnicfTerminalUserName'
_C='Integer32'
_B='HPN-ICF-UI-MAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfUIMgt=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,2))
_HpnicfUIMgtObjects_ObjectIdentity=ObjectIdentity
hpnicfUIMgtObjects=_HpnicfUIMgtObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,2,1))
_HpnicfUIBasicInfo_ObjectIdentity=ObjectIdentity
hpnicfUIBasicInfo=_HpnicfUIBasicInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,2,1,1))
_HpnicfUIScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfUIScalarObjects=_HpnicfUIScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,2,1,1,1))
_HpnicfUITrapBindObjects_ObjectIdentity=ObjectIdentity
hpnicfUITrapBindObjects=_HpnicfUITrapBindObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,2,1,1,2))
_HpnicfTerminalUserName_Type=DisplayString
_HpnicfTerminalUserName_Object=MibScalar
hpnicfTerminalUserName=_HpnicfTerminalUserName_Object((1,3,6,1,4,1,11,2,14,11,15,2,2,1,1,2,1),_HpnicfTerminalUserName_Type())
hpnicfTerminalUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTerminalUserName.setStatus(_A)
_HpnicfTerminalSource_Type=DisplayString
_HpnicfTerminalSource_Object=MibScalar
hpnicfTerminalSource=_HpnicfTerminalSource_Object((1,3,6,1,4,1,11,2,14,11,15,2,2,1,1,2,2),_HpnicfTerminalSource_Type())
hpnicfTerminalSource.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTerminalSource.setStatus(_A)
class _HpnicfTerminalUserAuthFailureReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('exceedRetries',1),('authTimeout',2),('otherReason',3)))
_HpnicfTerminalUserAuthFailureReason_Type.__name__=_C
_HpnicfTerminalUserAuthFailureReason_Object=MibScalar
hpnicfTerminalUserAuthFailureReason=_HpnicfTerminalUserAuthFailureReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,2,1,1,2,3),_HpnicfTerminalUserAuthFailureReason_Type())
hpnicfTerminalUserAuthFailureReason.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTerminalUserAuthFailureReason.setStatus(_A)
_HpnicfUINotifications_ObjectIdentity=ObjectIdentity
hpnicfUINotifications=_HpnicfUINotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,2,1,1,3))
_HpnicfUINotificationsPrefix_ObjectIdentity=ObjectIdentity
hpnicfUINotificationsPrefix=_HpnicfUINotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,2,1,1,3,0))
_HpnicfVtyMan_ObjectIdentity=ObjectIdentity
hpnicfVtyMan=_HpnicfVtyMan_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,2,1,2))
_HpnicfVtyAccTable_Object=MibTable
hpnicfVtyAccTable=_HpnicfVtyAccTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,2,1,2,1))
if mibBuilder.loadTexts:hpnicfVtyAccTable.setStatus(_A)
_HpnicfVtyAccEntry_Object=MibTableRow
hpnicfVtyAccEntry=_HpnicfVtyAccEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,2,1,2,1,1))
hpnicfVtyAccEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:hpnicfVtyAccEntry.setStatus(_A)
class _HpnicfVtyAccUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfVtyAccUserIndex_Type.__name__=_C
_HpnicfVtyAccUserIndex_Object=MibTableColumn
hpnicfVtyAccUserIndex=_HpnicfVtyAccUserIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,2,1,2,1,1,1),_HpnicfVtyAccUserIndex_Type())
hpnicfVtyAccUserIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfVtyAccUserIndex.setStatus(_A)
class _HpnicfVtyAccConnway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,11,12)));namedValues=NamedValues(*(('inbound',1),('outbound',2),('linkinbound',3),('acl6inbound',11),('acl6outbound',12)))
_HpnicfVtyAccConnway_Type.__name__=_C
_HpnicfVtyAccConnway_Object=MibTableColumn
hpnicfVtyAccConnway=_HpnicfVtyAccConnway_Object((1,3,6,1,4,1,11,2,14,11,15,2,2,1,2,1,1,2),_HpnicfVtyAccConnway_Type())
hpnicfVtyAccConnway.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfVtyAccConnway.setStatus(_A)
_HpnicfVtyAccAclNum_Type=Integer32
_HpnicfVtyAccAclNum_Object=MibTableColumn
hpnicfVtyAccAclNum=_HpnicfVtyAccAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,2,1,2,1,1,3),_HpnicfVtyAccAclNum_Type())
hpnicfVtyAccAclNum.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfVtyAccAclNum.setStatus(_A)
_HpnicfVtyAccEntryRowStatus_Type=RowStatus
_HpnicfVtyAccEntryRowStatus_Object=MibTableColumn
hpnicfVtyAccEntryRowStatus=_HpnicfVtyAccEntryRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,2,1,2,1,1,4),_HpnicfVtyAccEntryRowStatus_Type())
hpnicfVtyAccEntryRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfVtyAccEntryRowStatus.setStatus(_A)
_HpnicfConStatus_ObjectIdentity=ObjectIdentity
hpnicfConStatus=_HpnicfConStatus_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,2,1,3))
_HpnicfConStatusTable_Object=MibTable
hpnicfConStatusTable=_HpnicfConStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,2,1,3,1))
if mibBuilder.loadTexts:hpnicfConStatusTable.setStatus(_A)
_HpnicfConStatusEntry_Object=MibTableRow
hpnicfConStatusEntry=_HpnicfConStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,2,1,3,1,1))
hpnicfConStatusEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:hpnicfConStatusEntry.setStatus(_A)
_HpnicfConUserIndex_Type=Integer32
_HpnicfConUserIndex_Object=MibTableColumn
hpnicfConUserIndex=_HpnicfConUserIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,2,1,3,1,1,1),_HpnicfConUserIndex_Type())
hpnicfConUserIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfConUserIndex.setStatus(_A)
class _HpnicfConReAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_HpnicfConReAuth_Type.__name__=_C
_HpnicfConReAuth_Object=MibTableColumn
hpnicfConReAuth=_HpnicfConReAuth_Object((1,3,6,1,4,1,11,2,14,11,15,2,2,1,3,1,1,2),_HpnicfConReAuth_Type())
hpnicfConReAuth.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfConReAuth.setStatus(_A)
_HpnicfUIMgtMIBConformance18_ObjectIdentity=ObjectIdentity
hpnicfUIMgtMIBConformance18=_HpnicfUIMgtMIBConformance18_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,2,2))
_HpnicfUIMgtMIBCompliances_ObjectIdentity=ObjectIdentity
hpnicfUIMgtMIBCompliances=_HpnicfUIMgtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,2,2,1))
_HpnicfUIMgtManMIBGroups_ObjectIdentity=ObjectIdentity
hpnicfUIMgtManMIBGroups=_HpnicfUIMgtManMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,2,2,2))
hpnicfUIMgtBasicGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,2,2,2,1))
hpnicfUIMgtBasicGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:hpnicfUIMgtBasicGroup.setStatus(_A)
hpnicfConStatusGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,2,2,2,2))
hpnicfConStatusGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:hpnicfConStatusGroup.setStatus(_A)
hpnicfLogIn=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,2,1,1,3,0,1))
hpnicfLogIn.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hpnicfLogIn.setStatus(_A)
hpnicfLogOut=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,2,1,1,3,0,2))
hpnicfLogOut.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hpnicfLogOut.setStatus(_A)
hpnicfLogInAuthenFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,2,1,1,3,0,3))
hpnicfLogInAuthenFailure.setObjects(*((_B,_D),(_B,_E),(_B,_N)))
if mibBuilder.loadTexts:hpnicfLogInAuthenFailure.setStatus(_A)
hpnicfUIMgtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,2,2,1,1))
hpnicfUIMgtMIBCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:hpnicfUIMgtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfUIMgt':hpnicfUIMgt,'hpnicfUIMgtObjects':hpnicfUIMgtObjects,'hpnicfUIBasicInfo':hpnicfUIBasicInfo,'hpnicfUIScalarObjects':hpnicfUIScalarObjects,'hpnicfUITrapBindObjects':hpnicfUITrapBindObjects,_D:hpnicfTerminalUserName,_E:hpnicfTerminalSource,_N:hpnicfTerminalUserAuthFailureReason,'hpnicfUINotifications':hpnicfUINotifications,'hpnicfUINotificationsPrefix':hpnicfUINotificationsPrefix,'hpnicfLogIn':hpnicfLogIn,'hpnicfLogOut':hpnicfLogOut,'hpnicfLogInAuthenFailure':hpnicfLogInAuthenFailure,'hpnicfVtyMan':hpnicfVtyMan,'hpnicfVtyAccTable':hpnicfVtyAccTable,'hpnicfVtyAccEntry':hpnicfVtyAccEntry,_H:hpnicfVtyAccUserIndex,_I:hpnicfVtyAccConnway,_L:hpnicfVtyAccAclNum,'hpnicfVtyAccEntryRowStatus':hpnicfVtyAccEntryRowStatus,'hpnicfConStatus':hpnicfConStatus,'hpnicfConStatusTable':hpnicfConStatusTable,'hpnicfConStatusEntry':hpnicfConStatusEntry,_K:hpnicfConUserIndex,_M:hpnicfConReAuth,'hpnicfUIMgtMIBConformance18':hpnicfUIMgtMIBConformance18,'hpnicfUIMgtMIBCompliances':hpnicfUIMgtMIBCompliances,'hpnicfUIMgtMIBCompliance':hpnicfUIMgtMIBCompliance,'hpnicfUIMgtManMIBGroups':hpnicfUIMgtManMIBGroups,_O:hpnicfUIMgtBasicGroup,_P:hpnicfConStatusGroup})