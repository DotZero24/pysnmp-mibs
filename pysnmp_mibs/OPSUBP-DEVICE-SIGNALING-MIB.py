_R='serverNotificationsGroup'
_Q='ubpNotifyObjectsGroup'
_P='ubpEAPSessionEnd'
_O='ubpEAPSessionStart'
_N='ubpNotifyEAPAccessPortEntityOpenFlag'
_M='ubpNotifyEAPSessionEndReason'
_L='ubpNotifyEAPSessionStartSignalSequenceNumber'
_K='ubpNotifyEAPUserRoles'
_J='ubpNotifyEAPUserGroupIdentifier'
_I='ubpNotifyEAPSignalSequenceNumber'
_H='ubpNotifyEAPUserIdentifier'
_G='ubpNotifyEAPAccessPortEntityIdentifier'
_F='ubpNotifyDeviceIdentifier'
_E='ubpNotifyDeviceIdentifierType'
_D='Integer32'
_C='accessible-for-notify'
_B='current'
_A='OPSUBP-DEVICE-SIGNALING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nortel,=mibBuilder.importSymbols('NORTEL-MIB','nortel')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
nnOpsUbpDeviceSignalingMIB=ModuleIdentity((1,3,6,1,4,1,562,42,5,1,3))
if mibBuilder.loadTexts:nnOpsUbpDeviceSignalingMIB.setRevisions(('2013-04-12 00:00',))
_NnOPSNetIDGroup_ObjectIdentity=ObjectIdentity
nnOPSNetIDGroup=_NnOPSNetIDGroup_ObjectIdentity((1,3,6,1,4,1,562,42))
if mibBuilder.loadTexts:nnOPSNetIDGroup.setStatus(_B)
_NnOPSMIBS_ObjectIdentity=ObjectIdentity
nnOPSMIBS=_NnOPSMIBS_ObjectIdentity((1,3,6,1,4,1,562,42,5))
if mibBuilder.loadTexts:nnOPSMIBS.setStatus(_B)
_NnOPSQoSRootOID_ObjectIdentity=ObjectIdentity
nnOPSQoSRootOID=_NnOPSQoSRootOID_ObjectIdentity((1,3,6,1,4,1,562,42,5,1))
if mibBuilder.loadTexts:nnOPSQoSRootOID.setStatus(_B)
_NnOpsUbpDeviceSignalingMIBObjects_ObjectIdentity=ObjectIdentity
nnOpsUbpDeviceSignalingMIBObjects=_NnOpsUbpDeviceSignalingMIBObjects_ObjectIdentity((1,3,6,1,4,1,562,42,5,1,3,1))
if mibBuilder.loadTexts:nnOpsUbpDeviceSignalingMIBObjects.setStatus(_B)
_UbpNotifyObjects_ObjectIdentity=ObjectIdentity
ubpNotifyObjects=_UbpNotifyObjects_ObjectIdentity((1,3,6,1,4,1,562,42,5,1,3,1,1))
if mibBuilder.loadTexts:ubpNotifyObjects.setStatus(_B)
class _UbpNotifyDeviceIdentifierType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('devicemgmtadd',1),('snmpengineid',2)))
_UbpNotifyDeviceIdentifierType_Type.__name__=_D
_UbpNotifyDeviceIdentifierType_Object=MibScalar
ubpNotifyDeviceIdentifierType=_UbpNotifyDeviceIdentifierType_Object((1,3,6,1,4,1,562,42,5,1,3,1,1,1),_UbpNotifyDeviceIdentifierType_Type())
ubpNotifyDeviceIdentifierType.setMaxAccess(_C)
if mibBuilder.loadTexts:ubpNotifyDeviceIdentifierType.setStatus(_B)
_UbpNotifyDeviceIdentifier_Type=DisplayString
_UbpNotifyDeviceIdentifier_Object=MibScalar
ubpNotifyDeviceIdentifier=_UbpNotifyDeviceIdentifier_Object((1,3,6,1,4,1,562,42,5,1,3,1,1,2),_UbpNotifyDeviceIdentifier_Type())
ubpNotifyDeviceIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:ubpNotifyDeviceIdentifier.setStatus(_B)
_UbpNotifyEAPAccessPortEntityIdentifier_Type=DisplayString
_UbpNotifyEAPAccessPortEntityIdentifier_Object=MibScalar
ubpNotifyEAPAccessPortEntityIdentifier=_UbpNotifyEAPAccessPortEntityIdentifier_Object((1,3,6,1,4,1,562,42,5,1,3,1,1,3),_UbpNotifyEAPAccessPortEntityIdentifier_Type())
ubpNotifyEAPAccessPortEntityIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:ubpNotifyEAPAccessPortEntityIdentifier.setStatus(_B)
_UbpNotifyEAPUserIdentifier_Type=DisplayString
_UbpNotifyEAPUserIdentifier_Object=MibScalar
ubpNotifyEAPUserIdentifier=_UbpNotifyEAPUserIdentifier_Object((1,3,6,1,4,1,562,42,5,1,3,1,1,4),_UbpNotifyEAPUserIdentifier_Type())
ubpNotifyEAPUserIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:ubpNotifyEAPUserIdentifier.setStatus(_B)
_UbpNotifyEAPUserGroupIdentifier_Type=DisplayString
_UbpNotifyEAPUserGroupIdentifier_Object=MibScalar
ubpNotifyEAPUserGroupIdentifier=_UbpNotifyEAPUserGroupIdentifier_Object((1,3,6,1,4,1,562,42,5,1,3,1,1,5),_UbpNotifyEAPUserGroupIdentifier_Type())
ubpNotifyEAPUserGroupIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:ubpNotifyEAPUserGroupIdentifier.setStatus(_B)
_UbpNotifyEAPUserRoles_Type=DisplayString
_UbpNotifyEAPUserRoles_Object=MibScalar
ubpNotifyEAPUserRoles=_UbpNotifyEAPUserRoles_Object((1,3,6,1,4,1,562,42,5,1,3,1,1,6),_UbpNotifyEAPUserRoles_Type())
ubpNotifyEAPUserRoles.setMaxAccess(_C)
if mibBuilder.loadTexts:ubpNotifyEAPUserRoles.setStatus(_B)
_UbpNotifyEAPSignalSequenceNumber_Type=Unsigned32
_UbpNotifyEAPSignalSequenceNumber_Object=MibScalar
ubpNotifyEAPSignalSequenceNumber=_UbpNotifyEAPSignalSequenceNumber_Object((1,3,6,1,4,1,562,42,5,1,3,1,1,7),_UbpNotifyEAPSignalSequenceNumber_Type())
ubpNotifyEAPSignalSequenceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ubpNotifyEAPSignalSequenceNumber.setStatus(_B)
_UbpNotifyEAPSessionStartSignalSequenceNumber_Type=Unsigned32
_UbpNotifyEAPSessionStartSignalSequenceNumber_Object=MibScalar
ubpNotifyEAPSessionStartSignalSequenceNumber=_UbpNotifyEAPSessionStartSignalSequenceNumber_Object((1,3,6,1,4,1,562,42,5,1,3,1,1,8),_UbpNotifyEAPSessionStartSignalSequenceNumber_Type())
ubpNotifyEAPSessionStartSignalSequenceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ubpNotifyEAPSessionStartSignalSequenceNumber.setStatus(_B)
class _UbpNotifyEAPSessionEndReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eapsessionEndUserlogoff',1),('eapsessionEndOther',2)))
_UbpNotifyEAPSessionEndReason_Type.__name__=_D
_UbpNotifyEAPSessionEndReason_Object=MibScalar
ubpNotifyEAPSessionEndReason=_UbpNotifyEAPSessionEndReason_Object((1,3,6,1,4,1,562,42,5,1,3,1,1,9),_UbpNotifyEAPSessionEndReason_Type())
ubpNotifyEAPSessionEndReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ubpNotifyEAPSessionEndReason.setStatus(_B)
class _UbpNotifyEAPAccessPortEntityOpenFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eapAccessPortFlagNotApplicable',1),('eapAccessPortOpenRequired',2),('eapAccessPortOpenNotRequired',3)))
_UbpNotifyEAPAccessPortEntityOpenFlag_Type.__name__=_D
_UbpNotifyEAPAccessPortEntityOpenFlag_Object=MibScalar
ubpNotifyEAPAccessPortEntityOpenFlag=_UbpNotifyEAPAccessPortEntityOpenFlag_Object((1,3,6,1,4,1,562,42,5,1,3,1,1,10),_UbpNotifyEAPAccessPortEntityOpenFlag_Type())
ubpNotifyEAPAccessPortEntityOpenFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ubpNotifyEAPAccessPortEntityOpenFlag.setStatus(_B)
_UbpDeviceSignalingMIBNotifications_ObjectIdentity=ObjectIdentity
ubpDeviceSignalingMIBNotifications=_UbpDeviceSignalingMIBNotifications_ObjectIdentity((1,3,6,1,4,1,562,42,5,1,3,2))
_NnOpsUbpDeviceSignalingMIBConformance_ObjectIdentity=ObjectIdentity
nnOpsUbpDeviceSignalingMIBConformance=_NnOpsUbpDeviceSignalingMIBConformance_ObjectIdentity((1,3,6,1,4,1,562,42,5,1,3,3))
if mibBuilder.loadTexts:nnOpsUbpDeviceSignalingMIBConformance.setStatus(_B)
_NnOpsUbpDeviceSignalingMIBCompliances_ObjectIdentity=ObjectIdentity
nnOpsUbpDeviceSignalingMIBCompliances=_NnOpsUbpDeviceSignalingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,562,42,5,1,3,3,1))
_NnOpsUbpDeviceSignalingMIBGroups_ObjectIdentity=ObjectIdentity
nnOpsUbpDeviceSignalingMIBGroups=_NnOpsUbpDeviceSignalingMIBGroups_ObjectIdentity((1,3,6,1,4,1,562,42,5,1,3,3,2))
ubpNotifyObjectsGroup=ObjectGroup((1,3,6,1,4,1,562,42,5,1,3,3,2,1))
ubpNotifyObjectsGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_J),(_A,_K),(_A,_I),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ubpNotifyObjectsGroup.setStatus(_B)
ubpEAPSessionStart=NotificationType((1,3,6,1,4,1,562,42,5,1,3,2,1))
ubpEAPSessionStart.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_J),(_A,_K),(_A,_I),(_A,_N)))
if mibBuilder.loadTexts:ubpEAPSessionStart.setStatus(_B)
ubpEAPSessionEnd=NotificationType((1,3,6,1,4,1,562,42,5,1,3,2,2))
ubpEAPSessionEnd.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_M),(_A,_I),(_A,_L)))
if mibBuilder.loadTexts:ubpEAPSessionEnd.setStatus(_B)
serverNotificationsGroup=NotificationGroup((1,3,6,1,4,1,562,42,5,1,3,3,2,2))
serverNotificationsGroup.setObjects(*((_A,_O),(_A,_P)))
if mibBuilder.loadTexts:serverNotificationsGroup.setStatus(_B)
nnOpsUbpDeviceSignalingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,562,42,5,1,3,3,1,1))
nnOpsUbpDeviceSignalingMIBCompliance.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:nnOpsUbpDeviceSignalingMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'nnOPSNetIDGroup':nnOPSNetIDGroup,'nnOPSMIBS':nnOPSMIBS,'nnOPSQoSRootOID':nnOPSQoSRootOID,'nnOpsUbpDeviceSignalingMIB':nnOpsUbpDeviceSignalingMIB,'nnOpsUbpDeviceSignalingMIBObjects':nnOpsUbpDeviceSignalingMIBObjects,'ubpNotifyObjects':ubpNotifyObjects,_E:ubpNotifyDeviceIdentifierType,_F:ubpNotifyDeviceIdentifier,_G:ubpNotifyEAPAccessPortEntityIdentifier,_H:ubpNotifyEAPUserIdentifier,_J:ubpNotifyEAPUserGroupIdentifier,_K:ubpNotifyEAPUserRoles,_I:ubpNotifyEAPSignalSequenceNumber,_L:ubpNotifyEAPSessionStartSignalSequenceNumber,_M:ubpNotifyEAPSessionEndReason,_N:ubpNotifyEAPAccessPortEntityOpenFlag,'ubpDeviceSignalingMIBNotifications':ubpDeviceSignalingMIBNotifications,_O:ubpEAPSessionStart,_P:ubpEAPSessionEnd,'nnOpsUbpDeviceSignalingMIBConformance':nnOpsUbpDeviceSignalingMIBConformance,'nnOpsUbpDeviceSignalingMIBCompliances':nnOpsUbpDeviceSignalingMIBCompliances,'nnOpsUbpDeviceSignalingMIBCompliance':nnOpsUbpDeviceSignalingMIBCompliance,'nnOpsUbpDeviceSignalingMIBGroups':nnOpsUbpDeviceSignalingMIBGroups,_Q:ubpNotifyObjectsGroup,_R:serverNotificationsGroup})