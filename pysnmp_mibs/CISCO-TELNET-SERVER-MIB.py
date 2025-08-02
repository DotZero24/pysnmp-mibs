_W='ctsSessionNotifsControlGroup'
_V='ctsMIBNotificationGroup'
_U='ctsMIBSessionsObjectGroup'
_T='ctsSessionLoginFailure'
_S='ctsSessionDenied'
_R='ctsSessionStarted'
_Q='ctsSessionEnded'
_P='ctsSessionFailureNotifEnable'
_O='ctsSessionDeniedNotifEnable'
_N='ctsSessionStartedNotifEnable'
_M='ctsSessionEndedNotifEnable'
_L='ctsSessionPID'
_K='ctsTelnetActivation'
_J='ctsSessionDescription'
_I='ctsSessionID'
_H='read-write'
_G='ctsSessionTcpPort'
_F='ctsSessionUserID'
_E='ctsSessionsClientAddress'
_D='ctsSessionClientAddressType'
_C='read-only'
_B='current'
_A='CISCO-TELNET-SERVER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoTelnetServerMIB=ModuleIdentity((1,3,6,1,4,1,9,9,630))
if mibBuilder.loadTexts:ciscoTelnetServerMIB.setRevisions(('2007-05-08 00:00',))
_CiscoTelnetServerMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoTelnetServerMIBNotifs=_CiscoTelnetServerMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,630,0))
_CiscoTelnetServerMIBObjects_ObjectIdentity=ObjectIdentity
ciscoTelnetServerMIBObjects=_CiscoTelnetServerMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,630,1))
_CiscoTelnetServerConfigObjects_ObjectIdentity=ObjectIdentity
ciscoTelnetServerConfigObjects=_CiscoTelnetServerConfigObjects_ObjectIdentity((1,3,6,1,4,1,9,9,630,1,1))
_CtsTelnetActivation_Type=TruthValue
_CtsTelnetActivation_Object=MibScalar
ctsTelnetActivation=_CtsTelnetActivation_Object((1,3,6,1,4,1,9,9,630,1,1,1),_CtsTelnetActivation_Type())
ctsTelnetActivation.setMaxAccess(_H)
if mibBuilder.loadTexts:ctsTelnetActivation.setStatus(_B)
_CtsSessionEndedNotifEnable_Type=TruthValue
_CtsSessionEndedNotifEnable_Object=MibScalar
ctsSessionEndedNotifEnable=_CtsSessionEndedNotifEnable_Object((1,3,6,1,4,1,9,9,630,1,1,2),_CtsSessionEndedNotifEnable_Type())
ctsSessionEndedNotifEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:ctsSessionEndedNotifEnable.setStatus(_B)
_CtsSessionStartedNotifEnable_Type=TruthValue
_CtsSessionStartedNotifEnable_Object=MibScalar
ctsSessionStartedNotifEnable=_CtsSessionStartedNotifEnable_Object((1,3,6,1,4,1,9,9,630,1,1,3),_CtsSessionStartedNotifEnable_Type())
ctsSessionStartedNotifEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:ctsSessionStartedNotifEnable.setStatus(_B)
_CtsSessionDeniedNotifEnable_Type=TruthValue
_CtsSessionDeniedNotifEnable_Object=MibScalar
ctsSessionDeniedNotifEnable=_CtsSessionDeniedNotifEnable_Object((1,3,6,1,4,1,9,9,630,1,1,4),_CtsSessionDeniedNotifEnable_Type())
ctsSessionDeniedNotifEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:ctsSessionDeniedNotifEnable.setStatus(_B)
_CtsSessionFailureNotifEnable_Type=TruthValue
_CtsSessionFailureNotifEnable_Object=MibScalar
ctsSessionFailureNotifEnable=_CtsSessionFailureNotifEnable_Object((1,3,6,1,4,1,9,9,630,1,1,5),_CtsSessionFailureNotifEnable_Type())
ctsSessionFailureNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ctsSessionFailureNotifEnable.setStatus(_B)
_CiscoTelnetServerStatusObjects_ObjectIdentity=ObjectIdentity
ciscoTelnetServerStatusObjects=_CiscoTelnetServerStatusObjects_ObjectIdentity((1,3,6,1,4,1,9,9,630,1,2))
_CtsSessionsTable_Object=MibTable
ctsSessionsTable=_CtsSessionsTable_Object((1,3,6,1,4,1,9,9,630,1,2,1))
if mibBuilder.loadTexts:ctsSessionsTable.setStatus(_B)
_CtsSessionsEntry_Object=MibTableRow
ctsSessionsEntry=_CtsSessionsEntry_Object((1,3,6,1,4,1,9,9,630,1,2,1,1))
ctsSessionsEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ctsSessionsEntry.setStatus(_B)
_CtsSessionID_Type=Unsigned32
_CtsSessionID_Object=MibTableColumn
ctsSessionID=_CtsSessionID_Object((1,3,6,1,4,1,9,9,630,1,2,1,1,1),_CtsSessionID_Type())
ctsSessionID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ctsSessionID.setStatus(_B)
_CtsSessionDescription_Type=SnmpAdminString
_CtsSessionDescription_Object=MibTableColumn
ctsSessionDescription=_CtsSessionDescription_Object((1,3,6,1,4,1,9,9,630,1,2,1,1,2),_CtsSessionDescription_Type())
ctsSessionDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ctsSessionDescription.setStatus(_B)
_CtsSessionClientAddressType_Type=InetAddressType
_CtsSessionClientAddressType_Object=MibTableColumn
ctsSessionClientAddressType=_CtsSessionClientAddressType_Object((1,3,6,1,4,1,9,9,630,1,2,1,1,3),_CtsSessionClientAddressType_Type())
ctsSessionClientAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctsSessionClientAddressType.setStatus(_B)
_CtsSessionsClientAddress_Type=InetAddress
_CtsSessionsClientAddress_Object=MibTableColumn
ctsSessionsClientAddress=_CtsSessionsClientAddress_Object((1,3,6,1,4,1,9,9,630,1,2,1,1,4),_CtsSessionsClientAddress_Type())
ctsSessionsClientAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctsSessionsClientAddress.setStatus(_B)
_CtsSessionPID_Type=Unsigned32
_CtsSessionPID_Object=MibTableColumn
ctsSessionPID=_CtsSessionPID_Object((1,3,6,1,4,1,9,9,630,1,2,1,1,5),_CtsSessionPID_Type())
ctsSessionPID.setMaxAccess(_C)
if mibBuilder.loadTexts:ctsSessionPID.setStatus(_B)
_CtsSessionUserID_Type=SnmpAdminString
_CtsSessionUserID_Object=MibTableColumn
ctsSessionUserID=_CtsSessionUserID_Object((1,3,6,1,4,1,9,9,630,1,2,1,1,6),_CtsSessionUserID_Type())
ctsSessionUserID.setMaxAccess(_C)
if mibBuilder.loadTexts:ctsSessionUserID.setStatus(_B)
_CtsSessionTcpPort_Type=InetPortNumber
_CtsSessionTcpPort_Object=MibTableColumn
ctsSessionTcpPort=_CtsSessionTcpPort_Object((1,3,6,1,4,1,9,9,630,1,2,1,1,7),_CtsSessionTcpPort_Type())
ctsSessionTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ctsSessionTcpPort.setStatus(_B)
_CiscoTelnetServerMIBConform_ObjectIdentity=ObjectIdentity
ciscoTelnetServerMIBConform=_CiscoTelnetServerMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,630,2))
_CiscoTelnetServerMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoTelnetServerMIBCompliances=_CiscoTelnetServerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,630,2,1))
_CiscoTelnetServerMIBGroups_ObjectIdentity=ObjectIdentity
ciscoTelnetServerMIBGroups=_CiscoTelnetServerMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,630,2,2))
ctsMIBSessionsObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,630,2,2,1))
ctsMIBSessionsObjectGroup.setObjects(*((_A,_J),(_A,_D),(_A,_E),(_A,_K),(_A,_L),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ctsMIBSessionsObjectGroup.setStatus(_B)
ctsSessionNotifsControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,630,2,2,3))
ctsSessionNotifsControlGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ctsSessionNotifsControlGroup.setStatus(_B)
ctsSessionEnded=NotificationType((1,3,6,1,4,1,9,9,630,0,1))
ctsSessionEnded.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ctsSessionEnded.setStatus(_B)
ctsSessionStarted=NotificationType((1,3,6,1,4,1,9,9,630,0,2))
ctsSessionStarted.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ctsSessionStarted.setStatus(_B)
ctsSessionDenied=NotificationType((1,3,6,1,4,1,9,9,630,0,3))
ctsSessionDenied.setObjects(*((_A,_D),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:ctsSessionDenied.setStatus(_B)
ctsSessionLoginFailure=NotificationType((1,3,6,1,4,1,9,9,630,0,4))
ctsSessionLoginFailure.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ctsSessionLoginFailure.setStatus(_B)
ctsMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,630,2,2,2))
ctsMIBNotificationGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ctsMIBNotificationGroup.setStatus(_B)
ciscoTelnetServerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,630,2,1,1))
ciscoTelnetServerMIBCompliance.setObjects(*((_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ciscoTelnetServerMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoTelnetServerMIB':ciscoTelnetServerMIB,'ciscoTelnetServerMIBNotifs':ciscoTelnetServerMIBNotifs,_Q:ctsSessionEnded,_R:ctsSessionStarted,_S:ctsSessionDenied,_T:ctsSessionLoginFailure,'ciscoTelnetServerMIBObjects':ciscoTelnetServerMIBObjects,'ciscoTelnetServerConfigObjects':ciscoTelnetServerConfigObjects,_K:ctsTelnetActivation,_M:ctsSessionEndedNotifEnable,_N:ctsSessionStartedNotifEnable,_O:ctsSessionDeniedNotifEnable,_P:ctsSessionFailureNotifEnable,'ciscoTelnetServerStatusObjects':ciscoTelnetServerStatusObjects,'ctsSessionsTable':ctsSessionsTable,'ctsSessionsEntry':ctsSessionsEntry,_I:ctsSessionID,_J:ctsSessionDescription,_D:ctsSessionClientAddressType,_E:ctsSessionsClientAddress,_L:ctsSessionPID,_F:ctsSessionUserID,_G:ctsSessionTcpPort,'ciscoTelnetServerMIBConform':ciscoTelnetServerMIBConform,'ciscoTelnetServerMIBCompliances':ciscoTelnetServerMIBCompliances,'ciscoTelnetServerMIBCompliance':ciscoTelnetServerMIBCompliance,'ciscoTelnetServerMIBGroups':ciscoTelnetServerMIBGroups,_U:ctsMIBSessionsObjectGroup,_V:ctsMIBNotificationGroup,_W:ctsSessionNotifsControlGroup})