_U='mxDebugPcmCaptureGroupVer1'
_T='mxDebugFaxGroupVer1'
_S='mxDebugSignalingLogGroupVer1'
_R='mxDebugPcmCaptureIpAddress'
_Q='mxDebugPcmCaptureEnable'
_P='mxDebugFaxRelayFromDspToSyslog'
_O='mxDebugFaxRelayForDspToSyslog'
_N='mxDebugT38IncomingToSyslog'
_M='mxDebugT38OutgoingToSyslog'
_L='mxDebugSignalingLogPort'
_K='mxDebugSignalingLogHost'
_J='mxDebugSignalingLogEnable'
_I='MxIpPort'
_H='MxIpHostName'
_G='Unsigned32'
_F='enable'
_E='disable'
_D='Integer32'
_C='MX-DEBUG-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixExperimental,=mibBuilder.importSymbols('MX-SMI','mediatrixExperimental')
MxIpHostName,MxIpPort=mibBuilder.importSymbols('MX-TC',_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mxDebugMIB=ModuleIdentity((1,3,6,1,4,1,4935,99,5))
if mibBuilder.loadTexts:mxDebugMIB.setRevisions(('1909-11-27 00:00','1908-08-22 00:00','1908-05-21 00:00','1907-10-24 00:00','1902-07-05 00:00'))
_MxDebugMIBObjects_ObjectIdentity=ObjectIdentity
mxDebugMIBObjects=_MxDebugMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,99,5,1))
_MxDebugSignalingLog_ObjectIdentity=ObjectIdentity
mxDebugSignalingLog=_MxDebugSignalingLog_ObjectIdentity((1,3,6,1,4,1,4935,99,5,1,5))
class _MxDebugSignalingLogEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MxDebugSignalingLogEnable_Type.__name__=_D
_MxDebugSignalingLogEnable_Object=MibScalar
mxDebugSignalingLogEnable=_MxDebugSignalingLogEnable_Object((1,3,6,1,4,1,4935,99,5,1,5,1),_MxDebugSignalingLogEnable_Type())
mxDebugSignalingLogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:mxDebugSignalingLogEnable.setStatus(_A)
class _MxDebugSignalingLogHost_Type(MxIpHostName):defaultValue=OctetString('192.168.0.10')
_MxDebugSignalingLogHost_Type.__name__=_H
_MxDebugSignalingLogHost_Object=MibScalar
mxDebugSignalingLogHost=_MxDebugSignalingLogHost_Object((1,3,6,1,4,1,4935,99,5,1,5,2),_MxDebugSignalingLogHost_Type())
mxDebugSignalingLogHost.setMaxAccess(_B)
if mibBuilder.loadTexts:mxDebugSignalingLogHost.setStatus(_A)
class _MxDebugSignalingLogPort_Type(MxIpPort):defaultValue=6000
_MxDebugSignalingLogPort_Type.__name__=_I
_MxDebugSignalingLogPort_Object=MibScalar
mxDebugSignalingLogPort=_MxDebugSignalingLogPort_Object((1,3,6,1,4,1,4935,99,5,1,5,3),_MxDebugSignalingLogPort_Type())
mxDebugSignalingLogPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mxDebugSignalingLogPort.setStatus(_A)
_MxDebugFax_ObjectIdentity=ObjectIdentity
mxDebugFax=_MxDebugFax_ObjectIdentity((1,3,6,1,4,1,4935,99,5,1,10))
class _MxDebugT38OutgoingToSyslog_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MxDebugT38OutgoingToSyslog_Type.__name__=_D
_MxDebugT38OutgoingToSyslog_Object=MibScalar
mxDebugT38OutgoingToSyslog=_MxDebugT38OutgoingToSyslog_Object((1,3,6,1,4,1,4935,99,5,1,10,5),_MxDebugT38OutgoingToSyslog_Type())
mxDebugT38OutgoingToSyslog.setMaxAccess(_B)
if mibBuilder.loadTexts:mxDebugT38OutgoingToSyslog.setStatus(_A)
class _MxDebugT38IncomingToSyslog_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MxDebugT38IncomingToSyslog_Type.__name__=_D
_MxDebugT38IncomingToSyslog_Object=MibScalar
mxDebugT38IncomingToSyslog=_MxDebugT38IncomingToSyslog_Object((1,3,6,1,4,1,4935,99,5,1,10,6),_MxDebugT38IncomingToSyslog_Type())
mxDebugT38IncomingToSyslog.setMaxAccess(_B)
if mibBuilder.loadTexts:mxDebugT38IncomingToSyslog.setStatus(_A)
class _MxDebugFaxRelayForDspToSyslog_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MxDebugFaxRelayForDspToSyslog_Type.__name__=_D
_MxDebugFaxRelayForDspToSyslog_Object=MibScalar
mxDebugFaxRelayForDspToSyslog=_MxDebugFaxRelayForDspToSyslog_Object((1,3,6,1,4,1,4935,99,5,1,10,15),_MxDebugFaxRelayForDspToSyslog_Type())
mxDebugFaxRelayForDspToSyslog.setMaxAccess(_B)
if mibBuilder.loadTexts:mxDebugFaxRelayForDspToSyslog.setStatus(_A)
class _MxDebugFaxRelayFromDspToSyslog_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MxDebugFaxRelayFromDspToSyslog_Type.__name__=_D
_MxDebugFaxRelayFromDspToSyslog_Object=MibScalar
mxDebugFaxRelayFromDspToSyslog=_MxDebugFaxRelayFromDspToSyslog_Object((1,3,6,1,4,1,4935,99,5,1,10,16),_MxDebugFaxRelayFromDspToSyslog_Type())
mxDebugFaxRelayFromDspToSyslog.setMaxAccess(_B)
if mibBuilder.loadTexts:mxDebugFaxRelayFromDspToSyslog.setStatus(_A)
_MxDebugPcmCapture_ObjectIdentity=ObjectIdentity
mxDebugPcmCapture=_MxDebugPcmCapture_ObjectIdentity((1,3,6,1,4,1,4935,99,5,1,60))
class _MxDebugPcmCaptureEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MxDebugPcmCaptureEnable_Type.__name__=_D
_MxDebugPcmCaptureEnable_Object=MibScalar
mxDebugPcmCaptureEnable=_MxDebugPcmCaptureEnable_Object((1,3,6,1,4,1,4935,99,5,1,60,5),_MxDebugPcmCaptureEnable_Type())
mxDebugPcmCaptureEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:mxDebugPcmCaptureEnable.setStatus(_A)
class _MxDebugPcmCaptureIpAddress_Type(MxIpHostName):defaultValue=OctetString('192.168.10.1')
_MxDebugPcmCaptureIpAddress_Type.__name__=_H
_MxDebugPcmCaptureIpAddress_Object=MibScalar
mxDebugPcmCaptureIpAddress=_MxDebugPcmCaptureIpAddress_Object((1,3,6,1,4,1,4935,99,5,1,60,10),_MxDebugPcmCaptureIpAddress_Type())
mxDebugPcmCaptureIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mxDebugPcmCaptureIpAddress.setStatus(_A)
class _MxDebugPcmCaptureEndpointNumber_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MxDebugPcmCaptureEndpointNumber_Type.__name__=_G
_MxDebugPcmCaptureEndpointNumber_Object=MibScalar
mxDebugPcmCaptureEndpointNumber=_MxDebugPcmCaptureEndpointNumber_Object((1,3,6,1,4,1,4935,99,5,1,60,20),_MxDebugPcmCaptureEndpointNumber_Type())
mxDebugPcmCaptureEndpointNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mxDebugPcmCaptureEndpointNumber.setStatus(_A)
_MxDebugDspStats_ObjectIdentity=ObjectIdentity
mxDebugDspStats=_MxDebugDspStats_ObjectIdentity((1,3,6,1,4,1,4935,99,5,1,70))
class _MxDebugDspStatsEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_MxDebugDspStatsEnable_Type.__name__=_D
_MxDebugDspStatsEnable_Object=MibScalar
mxDebugDspStatsEnable=_MxDebugDspStatsEnable_Object((1,3,6,1,4,1,4935,99,5,1,70,5),_MxDebugDspStatsEnable_Type())
mxDebugDspStatsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:mxDebugDspStatsEnable.setStatus(_A)
class _MxDebugDspStatsInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_MxDebugDspStatsInterval_Type.__name__=_G
_MxDebugDspStatsInterval_Object=MibScalar
mxDebugDspStatsInterval=_MxDebugDspStatsInterval_Object((1,3,6,1,4,1,4935,99,5,1,70,10),_MxDebugDspStatsInterval_Type())
mxDebugDspStatsInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:mxDebugDspStatsInterval.setStatus(_A)
class _MxDebugDspStatsFilter_Type(Unsigned32):defaultValue=0
_MxDebugDspStatsFilter_Type.__name__=_G
_MxDebugDspStatsFilter_Object=MibScalar
mxDebugDspStatsFilter=_MxDebugDspStatsFilter_Object((1,3,6,1,4,1,4935,99,5,1,70,15),_MxDebugDspStatsFilter_Type())
mxDebugDspStatsFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:mxDebugDspStatsFilter.setStatus(_A)
_MxDebugConformance_ObjectIdentity=ObjectIdentity
mxDebugConformance=_MxDebugConformance_ObjectIdentity((1,3,6,1,4,1,4935,99,5,2))
_MxDebugCompliances_ObjectIdentity=ObjectIdentity
mxDebugCompliances=_MxDebugCompliances_ObjectIdentity((1,3,6,1,4,1,4935,99,5,2,1))
_MxDebugGroups_ObjectIdentity=ObjectIdentity
mxDebugGroups=_MxDebugGroups_ObjectIdentity((1,3,6,1,4,1,4935,99,5,2,2))
mxDebugSignalingLogGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,5,2,2,10))
mxDebugSignalingLogGroupVer1.setObjects(*((_C,_J),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:mxDebugSignalingLogGroupVer1.setStatus(_A)
mxDebugFaxGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,5,2,2,20))
mxDebugFaxGroupVer1.setObjects(*((_C,_M),(_C,_N),(_C,_O),(_C,_P)))
if mibBuilder.loadTexts:mxDebugFaxGroupVer1.setStatus(_A)
mxDebugPcmCaptureGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,5,2,2,30))
mxDebugPcmCaptureGroupVer1.setObjects(*((_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:mxDebugPcmCaptureGroupVer1.setStatus(_A)
mxDebugComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,99,5,2,1,10))
mxDebugComplVer1.setObjects(*((_C,_S),(_C,_T),(_C,_U)))
if mibBuilder.loadTexts:mxDebugComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mxDebugMIB':mxDebugMIB,'mxDebugMIBObjects':mxDebugMIBObjects,'mxDebugSignalingLog':mxDebugSignalingLog,_J:mxDebugSignalingLogEnable,_K:mxDebugSignalingLogHost,_L:mxDebugSignalingLogPort,'mxDebugFax':mxDebugFax,_M:mxDebugT38OutgoingToSyslog,_N:mxDebugT38IncomingToSyslog,_O:mxDebugFaxRelayForDspToSyslog,_P:mxDebugFaxRelayFromDspToSyslog,'mxDebugPcmCapture':mxDebugPcmCapture,_Q:mxDebugPcmCaptureEnable,_R:mxDebugPcmCaptureIpAddress,'mxDebugPcmCaptureEndpointNumber':mxDebugPcmCaptureEndpointNumber,'mxDebugDspStats':mxDebugDspStats,'mxDebugDspStatsEnable':mxDebugDspStatsEnable,'mxDebugDspStatsInterval':mxDebugDspStatsInterval,'mxDebugDspStatsFilter':mxDebugDspStatsFilter,'mxDebugConformance':mxDebugConformance,'mxDebugCompliances':mxDebugCompliances,'mxDebugComplVer1':mxDebugComplVer1,'mxDebugGroups':mxDebugGroups,_S:mxDebugSignalingLogGroupVer1,_T:mxDebugFaxGroupVer1,_U:mxDebugPcmCaptureGroupVer1})