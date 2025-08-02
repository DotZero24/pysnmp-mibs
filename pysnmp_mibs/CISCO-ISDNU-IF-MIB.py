_W='ciuIfMIBGroup'
_V='ciuIfEnableULoopStatusNotification'
_U='ciuIfExternalSTPortStatus'
_T='ciuIfNebeErrors'
_S='ciuIfFebeErrors'
_R='ciuIfOverHeadBits'
_Q='ciuIfEocCommand'
_P='ciuIfStatus'
_O='ciuIfType'
_N='ciuIfExternalSTPortNumber'
_M='deactivated'
_L='activationPending'
_K='activated'
_J='TruthValue'
_I='DisplayString'
_H='OctetString'
_G='ciuIfLoopStatus'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='CISCO-ISDNU-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention',_J)
ciscoIsdnuIfMIB=ModuleIdentity((1,3,6,1,4,1,9,9,18))
_CiuIfObjects_ObjectIdentity=ObjectIdentity
ciuIfObjects=_CiuIfObjects_ObjectIdentity((1,3,6,1,4,1,9,9,18,1))
_CiuInterface_ObjectIdentity=ObjectIdentity
ciuInterface=_CiuInterface_ObjectIdentity((1,3,6,1,4,1,9,9,18,1,1))
_CiuIfStaticConfigTable_Object=MibTable
ciuIfStaticConfigTable=_CiuIfStaticConfigTable_Object((1,3,6,1,4,1,9,9,18,1,1,1))
if mibBuilder.loadTexts:ciuIfStaticConfigTable.setStatus(_A)
_CiuIfStaticConfigEntry_Object=MibTableRow
ciuIfStaticConfigEntry=_CiuIfStaticConfigEntry_Object((1,3,6,1,4,1,9,9,18,1,1,1,1))
ciuIfStaticConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ciuIfStaticConfigEntry.setStatus(_A)
class _CiuIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('addOnU',2),('onBoardU',3),('onBoardIntegUandSTPort',4),('addOnIntegUandSTPort',5)))
_CiuIfType_Type.__name__=_D
_CiuIfType_Object=MibTableColumn
ciuIfType=_CiuIfType_Object((1,3,6,1,4,1,9,9,18,1,1,1,1,1),_CiuIfType_Type())
ciuIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuIfType.setStatus(_A)
_CiuIfStatusTable_Object=MibTable
ciuIfStatusTable=_CiuIfStatusTable_Object((1,3,6,1,4,1,9,9,18,1,1,2))
if mibBuilder.loadTexts:ciuIfStatusTable.setStatus(_A)
_CiuIfStatusEntry_Object=MibTableRow
ciuIfStatusEntry=_CiuIfStatusEntry_Object((1,3,6,1,4,1,9,9,18,1,1,2,1))
ciuIfStatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ciuIfStatusEntry.setStatus(_A)
class _CiuIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_CiuIfStatus_Type.__name__=_D
_CiuIfStatus_Object=MibTableColumn
ciuIfStatus=_CiuIfStatus_Object((1,3,6,1,4,1,9,9,18,1,1,2,1,1),_CiuIfStatus_Type())
ciuIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuIfStatus.setStatus(_A)
class _CiuIfEocCommand_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_CiuIfEocCommand_Type.__name__=_I
_CiuIfEocCommand_Object=MibTableColumn
ciuIfEocCommand=_CiuIfEocCommand_Object((1,3,6,1,4,1,9,9,18,1,1,2,1,2),_CiuIfEocCommand_Type())
ciuIfEocCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuIfEocCommand.setStatus(_A)
class _CiuIfOverHeadBits_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CiuIfOverHeadBits_Type.__name__=_H
_CiuIfOverHeadBits_Object=MibTableColumn
ciuIfOverHeadBits=_CiuIfOverHeadBits_Object((1,3,6,1,4,1,9,9,18,1,1,2,1,3),_CiuIfOverHeadBits_Type())
ciuIfOverHeadBits.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuIfOverHeadBits.setStatus(_A)
_CiuIfFebeErrors_Type=Counter32
_CiuIfFebeErrors_Object=MibTableColumn
ciuIfFebeErrors=_CiuIfFebeErrors_Object((1,3,6,1,4,1,9,9,18,1,1,2,1,4),_CiuIfFebeErrors_Type())
ciuIfFebeErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuIfFebeErrors.setStatus(_A)
_CiuIfNebeErrors_Type=Counter32
_CiuIfNebeErrors_Object=MibTableColumn
ciuIfNebeErrors=_CiuIfNebeErrors_Object((1,3,6,1,4,1,9,9,18,1,1,2,1,5),_CiuIfNebeErrors_Type())
ciuIfNebeErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuIfNebeErrors.setStatus(_A)
class _CiuIfLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('type2Loopback',2),('type3Loopback',3),('ntQuietMode',4),('ilmtMode',5)))
_CiuIfLoopStatus_Type.__name__=_D
_CiuIfLoopStatus_Object=MibTableColumn
ciuIfLoopStatus=_CiuIfLoopStatus_Object((1,3,6,1,4,1,9,9,18,1,1,2,1,6),_CiuIfLoopStatus_Type())
ciuIfLoopStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuIfLoopStatus.setStatus(_A)
_CiuIfExternalSTPort_ObjectIdentity=ObjectIdentity
ciuIfExternalSTPort=_CiuIfExternalSTPort_ObjectIdentity((1,3,6,1,4,1,9,9,18,1,2))
_CiuIfExternalSTPortStatusTable_Object=MibTable
ciuIfExternalSTPortStatusTable=_CiuIfExternalSTPortStatusTable_Object((1,3,6,1,4,1,9,9,18,1,2,1))
if mibBuilder.loadTexts:ciuIfExternalSTPortStatusTable.setStatus(_A)
_CiuIfExternalSTPortStatusEntry_Object=MibTableRow
ciuIfExternalSTPortStatusEntry=_CiuIfExternalSTPortStatusEntry_Object((1,3,6,1,4,1,9,9,18,1,2,1,1))
ciuIfExternalSTPortStatusEntry.setIndexNames((0,_E,_F),(0,_B,_N))
if mibBuilder.loadTexts:ciuIfExternalSTPortStatusEntry.setStatus(_A)
class _CiuIfExternalSTPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CiuIfExternalSTPortNumber_Type.__name__=_D
_CiuIfExternalSTPortNumber_Object=MibTableColumn
ciuIfExternalSTPortNumber=_CiuIfExternalSTPortNumber_Object((1,3,6,1,4,1,9,9,18,1,2,1,1,1),_CiuIfExternalSTPortNumber_Type())
ciuIfExternalSTPortNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciuIfExternalSTPortNumber.setStatus(_A)
class _CiuIfExternalSTPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_CiuIfExternalSTPortStatus_Type.__name__=_D
_CiuIfExternalSTPortStatus_Object=MibTableColumn
ciuIfExternalSTPortStatus=_CiuIfExternalSTPortStatus_Object((1,3,6,1,4,1,9,9,18,1,2,1,1,2),_CiuIfExternalSTPortStatus_Type())
ciuIfExternalSTPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciuIfExternalSTPortStatus.setStatus(_A)
_CiuIfMIBNotificationEnables_ObjectIdentity=ObjectIdentity
ciuIfMIBNotificationEnables=_CiuIfMIBNotificationEnables_ObjectIdentity((1,3,6,1,4,1,9,9,18,1,3))
class _CiuIfEnableULoopStatusNotification_Type(TruthValue):defaultValue=2
_CiuIfEnableULoopStatusNotification_Type.__name__=_J
_CiuIfEnableULoopStatusNotification_Object=MibScalar
ciuIfEnableULoopStatusNotification=_CiuIfEnableULoopStatusNotification_Object((1,3,6,1,4,1,9,9,18,1,3,1),_CiuIfEnableULoopStatusNotification_Type())
ciuIfEnableULoopStatusNotification.setMaxAccess('read-write')
if mibBuilder.loadTexts:ciuIfEnableULoopStatusNotification.setStatus(_A)
_CiuIfMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciuIfMIBNotificationPrefix=_CiuIfMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,18,2))
_CiuIfMIBNotifications_ObjectIdentity=ObjectIdentity
ciuIfMIBNotifications=_CiuIfMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,18,2,0))
_CiuIfMIBConformance_ObjectIdentity=ObjectIdentity
ciuIfMIBConformance=_CiuIfMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,18,3))
_CiuIfMIBCompliances_ObjectIdentity=ObjectIdentity
ciuIfMIBCompliances=_CiuIfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,18,3,1))
_CiuIfMIBGroups_ObjectIdentity=ObjectIdentity
ciuIfMIBGroups=_CiuIfMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,18,3,2))
ciuIfMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,18,3,2,1))
ciuIfMIBGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_G),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:ciuIfMIBGroup.setStatus(_A)
ciuIfLoopStatusNotification=NotificationType((1,3,6,1,4,1,9,9,18,2,0,1))
ciuIfLoopStatusNotification.setObjects((_B,_G))
if mibBuilder.loadTexts:ciuIfLoopStatusNotification.setStatus(_A)
ciuIfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,18,3,1,1))
ciuIfMIBCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:ciuIfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIsdnuIfMIB':ciscoIsdnuIfMIB,'ciuIfObjects':ciuIfObjects,'ciuInterface':ciuInterface,'ciuIfStaticConfigTable':ciuIfStaticConfigTable,'ciuIfStaticConfigEntry':ciuIfStaticConfigEntry,_O:ciuIfType,'ciuIfStatusTable':ciuIfStatusTable,'ciuIfStatusEntry':ciuIfStatusEntry,_P:ciuIfStatus,_Q:ciuIfEocCommand,_R:ciuIfOverHeadBits,_S:ciuIfFebeErrors,_T:ciuIfNebeErrors,_G:ciuIfLoopStatus,'ciuIfExternalSTPort':ciuIfExternalSTPort,'ciuIfExternalSTPortStatusTable':ciuIfExternalSTPortStatusTable,'ciuIfExternalSTPortStatusEntry':ciuIfExternalSTPortStatusEntry,_N:ciuIfExternalSTPortNumber,_U:ciuIfExternalSTPortStatus,'ciuIfMIBNotificationEnables':ciuIfMIBNotificationEnables,_V:ciuIfEnableULoopStatusNotification,'ciuIfMIBNotificationPrefix':ciuIfMIBNotificationPrefix,'ciuIfMIBNotifications':ciuIfMIBNotifications,'ciuIfLoopStatusNotification':ciuIfLoopStatusNotification,'ciuIfMIBConformance':ciuIfMIBConformance,'ciuIfMIBCompliances':ciuIfMIBCompliances,'ciuIfMIBCompliance':ciuIfMIBCompliance,'ciuIfMIBGroups':ciuIfMIBGroups,_W:ciuIfMIBGroup})