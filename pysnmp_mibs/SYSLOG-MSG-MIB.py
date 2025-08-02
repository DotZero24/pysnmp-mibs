_d='syslogMsgNotification'
_c='syslogMsgEnableNotifications'
_b='syslogMsgTableMaxSize'
_a='syslogMsgSDParamValue'
_Z='syslogMsgSDParamName'
_Y='syslogMsgSDID'
_X='syslogMsgSDParamIndex'
_W='read-write'
_V='TruthValue'
_U='syslogMsgControlGroup'
_T='syslogMsgMsg'
_S='syslogMsgSDParams'
_R='syslogMsgMsgID'
_Q='syslogMsgProcID'
_P='syslogMsgAppName'
_O='syslogMsgHostName'
_N='syslogMsgTimeStamp'
_M='syslogMsgVersion'
_L='syslogMsgSeverity'
_K='syslogMsgFacility'
_J='syslogMsgIndex'
_I='syslogMsgNotificationGroup'
_H='syslogMsgSDGroup'
_G='syslogMsgGroup'
_F='not-accessible'
_E='Unsigned32'
_D='DisplayString'
_C='read-only'
_B='current'
_A='SYSLOG-MSG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention',_V)
SyslogFacility,SyslogSeverity=mibBuilder.importSymbols('SYSLOG-TC-MIB','SyslogFacility','SyslogSeverity')
syslogMsgMib=ModuleIdentity((1,3,6,1,2,1,192))
if mibBuilder.loadTexts:syslogMsgMib.setRevisions(('2009-08-13 08:00',))
class SyslogTimeStamp(TextualConvention,OctetString):status=_B;displayHint='2d-1d-1d,1d:1d:1d.3d,1a1d:1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(10,10),ValueSizeConstraint(13,13))
class SyslogParamValueString(TextualConvention,OctetString):status=_B;displayHint='65535t'
_SyslogMsgNotifications_ObjectIdentity=ObjectIdentity
syslogMsgNotifications=_SyslogMsgNotifications_ObjectIdentity((1,3,6,1,2,1,192,0))
_SyslogMsgObjects_ObjectIdentity=ObjectIdentity
syslogMsgObjects=_SyslogMsgObjects_ObjectIdentity((1,3,6,1,2,1,192,1))
_SyslogMsgControl_ObjectIdentity=ObjectIdentity
syslogMsgControl=_SyslogMsgControl_ObjectIdentity((1,3,6,1,2,1,192,1,1))
class _SyslogMsgTableMaxSize_Type(Unsigned32):defaultValue=0
_SyslogMsgTableMaxSize_Type.__name__=_E
_SyslogMsgTableMaxSize_Object=MibScalar
syslogMsgTableMaxSize=_SyslogMsgTableMaxSize_Object((1,3,6,1,2,1,192,1,1,1),_SyslogMsgTableMaxSize_Type())
syslogMsgTableMaxSize.setMaxAccess(_W)
if mibBuilder.loadTexts:syslogMsgTableMaxSize.setStatus(_B)
class _SyslogMsgEnableNotifications_Type(TruthValue):defaultValue=2
_SyslogMsgEnableNotifications_Type.__name__=_V
_SyslogMsgEnableNotifications_Object=MibScalar
syslogMsgEnableNotifications=_SyslogMsgEnableNotifications_Object((1,3,6,1,2,1,192,1,1,2),_SyslogMsgEnableNotifications_Type())
syslogMsgEnableNotifications.setMaxAccess(_W)
if mibBuilder.loadTexts:syslogMsgEnableNotifications.setStatus(_B)
_SyslogMsgTable_Object=MibTable
syslogMsgTable=_SyslogMsgTable_Object((1,3,6,1,2,1,192,1,2))
if mibBuilder.loadTexts:syslogMsgTable.setStatus(_B)
_SyslogMsgEntry_Object=MibTableRow
syslogMsgEntry=_SyslogMsgEntry_Object((1,3,6,1,2,1,192,1,2,1))
syslogMsgEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:syslogMsgEntry.setStatus(_B)
class _SyslogMsgIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SyslogMsgIndex_Type.__name__=_E
_SyslogMsgIndex_Object=MibTableColumn
syslogMsgIndex=_SyslogMsgIndex_Object((1,3,6,1,2,1,192,1,2,1,1),_SyslogMsgIndex_Type())
syslogMsgIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:syslogMsgIndex.setStatus(_B)
_SyslogMsgFacility_Type=SyslogFacility
_SyslogMsgFacility_Object=MibTableColumn
syslogMsgFacility=_SyslogMsgFacility_Object((1,3,6,1,2,1,192,1,2,1,2),_SyslogMsgFacility_Type())
syslogMsgFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgFacility.setStatus(_B)
_SyslogMsgSeverity_Type=SyslogSeverity
_SyslogMsgSeverity_Object=MibTableColumn
syslogMsgSeverity=_SyslogMsgSeverity_Object((1,3,6,1,2,1,192,1,2,1,3),_SyslogMsgSeverity_Type())
syslogMsgSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgSeverity.setStatus(_B)
class _SyslogMsgVersion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_SyslogMsgVersion_Type.__name__=_E
_SyslogMsgVersion_Object=MibTableColumn
syslogMsgVersion=_SyslogMsgVersion_Object((1,3,6,1,2,1,192,1,2,1,4),_SyslogMsgVersion_Type())
syslogMsgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgVersion.setStatus(_B)
_SyslogMsgTimeStamp_Type=SyslogTimeStamp
_SyslogMsgTimeStamp_Object=MibTableColumn
syslogMsgTimeStamp=_SyslogMsgTimeStamp_Object((1,3,6,1,2,1,192,1,2,1,5),_SyslogMsgTimeStamp_Type())
syslogMsgTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgTimeStamp.setStatus(_B)
class _SyslogMsgHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SyslogMsgHostName_Type.__name__=_D
_SyslogMsgHostName_Object=MibTableColumn
syslogMsgHostName=_SyslogMsgHostName_Object((1,3,6,1,2,1,192,1,2,1,6),_SyslogMsgHostName_Type())
syslogMsgHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgHostName.setStatus(_B)
class _SyslogMsgAppName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_SyslogMsgAppName_Type.__name__=_D
_SyslogMsgAppName_Object=MibTableColumn
syslogMsgAppName=_SyslogMsgAppName_Object((1,3,6,1,2,1,192,1,2,1,7),_SyslogMsgAppName_Type())
syslogMsgAppName.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgAppName.setStatus(_B)
class _SyslogMsgProcID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SyslogMsgProcID_Type.__name__=_D
_SyslogMsgProcID_Object=MibTableColumn
syslogMsgProcID=_SyslogMsgProcID_Object((1,3,6,1,2,1,192,1,2,1,8),_SyslogMsgProcID_Type())
syslogMsgProcID.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgProcID.setStatus(_B)
class _SyslogMsgMsgID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SyslogMsgMsgID_Type.__name__=_D
_SyslogMsgMsgID_Object=MibTableColumn
syslogMsgMsgID=_SyslogMsgMsgID_Object((1,3,6,1,2,1,192,1,2,1,9),_SyslogMsgMsgID_Type())
syslogMsgMsgID.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgMsgID.setStatus(_B)
_SyslogMsgSDParams_Type=Unsigned32
_SyslogMsgSDParams_Object=MibTableColumn
syslogMsgSDParams=_SyslogMsgSDParams_Object((1,3,6,1,2,1,192,1,2,1,10),_SyslogMsgSDParams_Type())
syslogMsgSDParams.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgSDParams.setStatus(_B)
_SyslogMsgMsg_Type=OctetString
_SyslogMsgMsg_Object=MibTableColumn
syslogMsgMsg=_SyslogMsgMsg_Object((1,3,6,1,2,1,192,1,2,1,11),_SyslogMsgMsg_Type())
syslogMsgMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgMsg.setStatus(_B)
_SyslogMsgSDTable_Object=MibTable
syslogMsgSDTable=_SyslogMsgSDTable_Object((1,3,6,1,2,1,192,1,3))
if mibBuilder.loadTexts:syslogMsgSDTable.setStatus(_B)
_SyslogMsgSDEntry_Object=MibTableRow
syslogMsgSDEntry=_SyslogMsgSDEntry_Object((1,3,6,1,2,1,192,1,3,1))
syslogMsgSDEntry.setIndexNames((0,_A,_J),(0,_A,_X),(0,_A,_Y),(0,_A,_Z))
if mibBuilder.loadTexts:syslogMsgSDEntry.setStatus(_B)
class _SyslogMsgSDParamIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SyslogMsgSDParamIndex_Type.__name__=_E
_SyslogMsgSDParamIndex_Object=MibTableColumn
syslogMsgSDParamIndex=_SyslogMsgSDParamIndex_Object((1,3,6,1,2,1,192,1,3,1,1),_SyslogMsgSDParamIndex_Type())
syslogMsgSDParamIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:syslogMsgSDParamIndex.setStatus(_B)
class _SyslogMsgSDID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SyslogMsgSDID_Type.__name__=_D
_SyslogMsgSDID_Object=MibTableColumn
syslogMsgSDID=_SyslogMsgSDID_Object((1,3,6,1,2,1,192,1,3,1,2),_SyslogMsgSDID_Type())
syslogMsgSDID.setMaxAccess(_F)
if mibBuilder.loadTexts:syslogMsgSDID.setStatus(_B)
class _SyslogMsgSDParamName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SyslogMsgSDParamName_Type.__name__=_D
_SyslogMsgSDParamName_Object=MibTableColumn
syslogMsgSDParamName=_SyslogMsgSDParamName_Object((1,3,6,1,2,1,192,1,3,1,3),_SyslogMsgSDParamName_Type())
syslogMsgSDParamName.setMaxAccess(_F)
if mibBuilder.loadTexts:syslogMsgSDParamName.setStatus(_B)
_SyslogMsgSDParamValue_Type=SyslogParamValueString
_SyslogMsgSDParamValue_Object=MibTableColumn
syslogMsgSDParamValue=_SyslogMsgSDParamValue_Object((1,3,6,1,2,1,192,1,3,1,4),_SyslogMsgSDParamValue_Type())
syslogMsgSDParamValue.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMsgSDParamValue.setStatus(_B)
_SyslogMsgConformance_ObjectIdentity=ObjectIdentity
syslogMsgConformance=_SyslogMsgConformance_ObjectIdentity((1,3,6,1,2,1,192,2))
_SyslogMsgGroups_ObjectIdentity=ObjectIdentity
syslogMsgGroups=_SyslogMsgGroups_ObjectIdentity((1,3,6,1,2,1,192,2,1))
_SyslogMsgCompliances_ObjectIdentity=ObjectIdentity
syslogMsgCompliances=_SyslogMsgCompliances_ObjectIdentity((1,3,6,1,2,1,192,2,2))
syslogMsgGroup=ObjectGroup((1,3,6,1,2,1,192,2,1,2))
syslogMsgGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:syslogMsgGroup.setStatus(_B)
syslogMsgSDGroup=ObjectGroup((1,3,6,1,2,1,192,2,1,3))
syslogMsgSDGroup.setObjects((_A,_a))
if mibBuilder.loadTexts:syslogMsgSDGroup.setStatus(_B)
syslogMsgControlGroup=ObjectGroup((1,3,6,1,2,1,192,2,1,4))
syslogMsgControlGroup.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:syslogMsgControlGroup.setStatus(_B)
syslogMsgNotification=NotificationType((1,3,6,1,2,1,192,0,1))
syslogMsgNotification.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:syslogMsgNotification.setStatus(_B)
syslogMsgNotificationGroup=NotificationGroup((1,3,6,1,2,1,192,2,1,1))
syslogMsgNotificationGroup.setObjects((_A,_d))
if mibBuilder.loadTexts:syslogMsgNotificationGroup.setStatus(_B)
syslogMsgFullCompliance=ModuleCompliance((1,3,6,1,2,1,192,2,2,1))
syslogMsgFullCompliance.setObjects(*((_A,_G),(_A,_H),(_A,_U),(_A,_I)))
if mibBuilder.loadTexts:syslogMsgFullCompliance.setStatus(_B)
syslogMsgReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,192,2,2,2))
syslogMsgReadOnlyCompliance.setObjects(*((_A,_G),(_A,_H),(_A,_U),(_A,_I)))
if mibBuilder.loadTexts:syslogMsgReadOnlyCompliance.setStatus(_B)
syslogMsgNotificationCompliance=ModuleCompliance((1,3,6,1,2,1,192,2,2,3))
syslogMsgNotificationCompliance.setObjects(*((_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:syslogMsgNotificationCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SyslogTimeStamp':SyslogTimeStamp,'SyslogParamValueString':SyslogParamValueString,'syslogMsgMib':syslogMsgMib,'syslogMsgNotifications':syslogMsgNotifications,_d:syslogMsgNotification,'syslogMsgObjects':syslogMsgObjects,'syslogMsgControl':syslogMsgControl,_b:syslogMsgTableMaxSize,_c:syslogMsgEnableNotifications,'syslogMsgTable':syslogMsgTable,'syslogMsgEntry':syslogMsgEntry,_J:syslogMsgIndex,_K:syslogMsgFacility,_L:syslogMsgSeverity,_M:syslogMsgVersion,_N:syslogMsgTimeStamp,_O:syslogMsgHostName,_P:syslogMsgAppName,_Q:syslogMsgProcID,_R:syslogMsgMsgID,_S:syslogMsgSDParams,_T:syslogMsgMsg,'syslogMsgSDTable':syslogMsgSDTable,'syslogMsgSDEntry':syslogMsgSDEntry,_X:syslogMsgSDParamIndex,_Y:syslogMsgSDID,_Z:syslogMsgSDParamName,_a:syslogMsgSDParamValue,'syslogMsgConformance':syslogMsgConformance,'syslogMsgGroups':syslogMsgGroups,_I:syslogMsgNotificationGroup,_G:syslogMsgGroup,_H:syslogMsgSDGroup,_U:syslogMsgControlGroup,'syslogMsgCompliances':syslogMsgCompliances,'syslogMsgFullCompliance':syslogMsgFullCompliance,'syslogMsgReadOnlyCompliance':syslogMsgReadOnlyCompliance,'syslogMsgNotificationCompliance':syslogMsgNotificationCompliance})