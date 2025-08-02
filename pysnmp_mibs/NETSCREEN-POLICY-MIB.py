_K='nsPlyMonVsys'
_J='nsPlyMonId'
_I='nsPlyId'
_H='nsPlyVsys'
_G='enabled'
_F='disable'
_E='NETSCREEN-POLICY-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenPolicy,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenPolicy')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
netscreenPolicyMibModule=ModuleIdentity((1,3,6,1,4,1,3224,10,0))
if mibBuilder.loadTexts:netscreenPolicyMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-08-13 00:00','2001-05-14 00:00'))
_NsPlyTable_Object=MibTable
nsPlyTable=_NsPlyTable_Object((1,3,6,1,4,1,3224,10,1))
if mibBuilder.loadTexts:nsPlyTable.setStatus(_A)
_NsPlyEntry_Object=MibTableRow
nsPlyEntry=_NsPlyEntry_Object((1,3,6,1,4,1,3224,10,1,1))
nsPlyEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:nsPlyEntry.setStatus(_A)
class _NsPlyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsPlyId_Type.__name__=_C
_NsPlyId_Object=MibTableColumn
nsPlyId=_NsPlyId_Object((1,3,6,1,4,1,3224,10,1,1,1),_NsPlyId_Type())
nsPlyId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyId.setStatus(_A)
class _NsPlyVsys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsPlyVsys_Type.__name__=_C
_NsPlyVsys_Object=MibTableColumn
nsPlyVsys=_NsPlyVsys_Object((1,3,6,1,4,1,3224,10,1,1,2),_NsPlyVsys_Type())
nsPlyVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyVsys.setStatus(_A)
class _NsPlySrcZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsPlySrcZone_Type.__name__=_D
_NsPlySrcZone_Object=MibTableColumn
nsPlySrcZone=_NsPlySrcZone_Object((1,3,6,1,4,1,3224,10,1,1,3),_NsPlySrcZone_Type())
nsPlySrcZone.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlySrcZone.setStatus(_A)
class _NsPlyDstZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsPlyDstZone_Type.__name__=_D
_NsPlyDstZone_Object=MibTableColumn
nsPlyDstZone=_NsPlyDstZone_Object((1,3,6,1,4,1,3224,10,1,1,4),_NsPlyDstZone_Type())
nsPlyDstZone.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyDstZone.setStatus(_A)
class _NsPlySrcAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsPlySrcAddr_Type.__name__=_D
_NsPlySrcAddr_Object=MibTableColumn
nsPlySrcAddr=_NsPlySrcAddr_Object((1,3,6,1,4,1,3224,10,1,1,5),_NsPlySrcAddr_Type())
nsPlySrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlySrcAddr.setStatus(_A)
class _NsPlyDstAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsPlyDstAddr_Type.__name__=_D
_NsPlyDstAddr_Object=MibTableColumn
nsPlyDstAddr=_NsPlyDstAddr_Object((1,3,6,1,4,1,3224,10,1,1,6),_NsPlyDstAddr_Type())
nsPlyDstAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyDstAddr.setStatus(_A)
class _NsPlyService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)));namedValues=NamedValues(*(('any',0),('aol',1),('bgp',2),('dpcp-relay',3),('dns',4),('finger',5),('ftp',6),('ftp-get',7),('ftp-put',8),('gopher',9),('h323',10),('http',11),('https',12),('icmp-info',13),('icmp-timestamp',14),('ike',15),('imap',16),('internet-locator-service',17),('irc',18),('l2tp',19),('ldap',20),('mail',21),('netmeeting',22),('nfs',23),('nntp',24),('ns-global',25),('ns-global-pro',26),('ntp',27),('ospf',28),('pc-anywhere',29),('ping',30),('pop3',31),('pptp',32),('real-media',33),('rip',34),('rlogin',35),('snmp',36),('ssh',37),('syslog',38),('talk',39),('tcp-any',40),('telnet',41),('tftp',42),('traceroute',43),('udp-any',44),('uucp',45),('vdo-live',46),('wais',47),('winframe',48),('x-windows',49),('other',50)))
_NsPlyService_Type.__name__=_C
_NsPlyService_Object=MibTableColumn
nsPlyService=_NsPlyService_Object((1,3,6,1,4,1,3224,10,1,1,7),_NsPlyService_Type())
nsPlyService.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyService.setStatus(_A)
class _NsPlyAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('deny',0),('permit',1),('tunnel',2)))
_NsPlyAction_Type.__name__=_C
_NsPlyAction_Object=MibTableColumn
nsPlyAction=_NsPlyAction_Object((1,3,6,1,4,1,3224,10,1,1,8),_NsPlyAction_Type())
nsPlyAction.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyAction.setStatus(_A)
class _NsPlyNat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NsPlyNat_Type.__name__=_C
_NsPlyNat_Object=MibTableColumn
nsPlyNat=_NsPlyNat_Object((1,3,6,1,4,1,3224,10,1,1,9),_NsPlyNat_Type())
nsPlyNat.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyNat.setStatus(_A)
class _NsPlyFixPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_NsPlyFixPort_Type.__name__=_C
_NsPlyFixPort_Object=MibTableColumn
nsPlyFixPort=_NsPlyFixPort_Object((1,3,6,1,4,1,3224,10,1,1,10),_NsPlyFixPort_Type())
nsPlyFixPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyFixPort.setStatus(_A)
_NsPlyDipId_Type=Integer32
_NsPlyDipId_Object=MibTableColumn
nsPlyDipId=_NsPlyDipId_Object((1,3,6,1,4,1,3224,10,1,1,11),_NsPlyDipId_Type())
nsPlyDipId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyDipId.setStatus(_A)
class _NsPlyVpnTunnel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsPlyVpnTunnel_Type.__name__=_D
_NsPlyVpnTunnel_Object=MibTableColumn
nsPlyVpnTunnel=_NsPlyVpnTunnel_Object((1,3,6,1,4,1,3224,10,1,1,12),_NsPlyVpnTunnel_Type())
nsPlyVpnTunnel.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyVpnTunnel.setStatus(_A)
class _NsPlyL2tpTunnel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsPlyL2tpTunnel_Type.__name__=_D
_NsPlyL2tpTunnel_Object=MibTableColumn
nsPlyL2tpTunnel=_NsPlyL2tpTunnel_Object((1,3,6,1,4,1,3224,10,1,1,13),_NsPlyL2tpTunnel_Type())
nsPlyL2tpTunnel.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyL2tpTunnel.setStatus(_A)
class _NsPlyAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NsPlyAuth_Type.__name__=_C
_NsPlyAuth_Object=MibTableColumn
nsPlyAuth=_NsPlyAuth_Object((1,3,6,1,4,1,3224,10,1,1,14),_NsPlyAuth_Type())
nsPlyAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyAuth.setStatus(_A)
class _NsPlyLogEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NsPlyLogEnable_Type.__name__=_C
_NsPlyLogEnable_Object=MibTableColumn
nsPlyLogEnable=_NsPlyLogEnable_Object((1,3,6,1,4,1,3224,10,1,1,15),_NsPlyLogEnable_Type())
nsPlyLogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyLogEnable.setStatus(_A)
class _NsPlyCountEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NsPlyCountEnable_Type.__name__=_C
_NsPlyCountEnable_Object=MibTableColumn
nsPlyCountEnable=_NsPlyCountEnable_Object((1,3,6,1,4,1,3224,10,1,1,16),_NsPlyCountEnable_Type())
nsPlyCountEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyCountEnable.setStatus(_A)
_NsPlyAlarmBPS_Type=Integer32
_NsPlyAlarmBPS_Object=MibTableColumn
nsPlyAlarmBPS=_NsPlyAlarmBPS_Object((1,3,6,1,4,1,3224,10,1,1,17),_NsPlyAlarmBPS_Type())
nsPlyAlarmBPS.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyAlarmBPS.setStatus(_A)
_NsPlyAlarmBPM_Type=Integer32
_NsPlyAlarmBPM_Object=MibTableColumn
nsPlyAlarmBPM=_NsPlyAlarmBPM_Object((1,3,6,1,4,1,3224,10,1,1,18),_NsPlyAlarmBPM_Type())
nsPlyAlarmBPM.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyAlarmBPM.setStatus(_A)
class _NsPlySchedule_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsPlySchedule_Type.__name__=_D
_NsPlySchedule_Object=MibTableColumn
nsPlySchedule=_NsPlySchedule_Object((1,3,6,1,4,1,3224,10,1,1,19),_NsPlySchedule_Type())
nsPlySchedule.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlySchedule.setStatus(_A)
class _NsPlyTrafficShapeEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_NsPlyTrafficShapeEnable_Type.__name__=_C
_NsPlyTrafficShapeEnable_Object=MibTableColumn
nsPlyTrafficShapeEnable=_NsPlyTrafficShapeEnable_Object((1,3,6,1,4,1,3224,10,1,1,20),_NsPlyTrafficShapeEnable_Type())
nsPlyTrafficShapeEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyTrafficShapeEnable.setStatus(_A)
class _NsPlyTrafficPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('high',0),('priority2nd',1),('priority3rd',2),('priority4th',3),('priority5th',4),('priority6th',5),('priority7th',6),('priorityLow',7)))
_NsPlyTrafficPriority_Type.__name__=_C
_NsPlyTrafficPriority_Object=MibTableColumn
nsPlyTrafficPriority=_NsPlyTrafficPriority_Object((1,3,6,1,4,1,3224,10,1,1,21),_NsPlyTrafficPriority_Type())
nsPlyTrafficPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyTrafficPriority.setStatus(_A)
class _NsPlyDSEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NsPlyDSEnable_Type.__name__=_C
_NsPlyDSEnable_Object=MibTableColumn
nsPlyDSEnable=_NsPlyDSEnable_Object((1,3,6,1,4,1,3224,10,1,1,22),_NsPlyDSEnable_Type())
nsPlyDSEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyDSEnable.setStatus(_A)
class _NsPlyActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('inactive',0),('inuse',1),('hidden',2)))
_NsPlyActiveStatus_Type.__name__=_C
_NsPlyActiveStatus_Object=MibTableColumn
nsPlyActiveStatus=_NsPlyActiveStatus_Object((1,3,6,1,4,1,3224,10,1,1,23),_NsPlyActiveStatus_Type())
nsPlyActiveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyActiveStatus.setStatus(_A)
class _NsPlyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsPlyName_Type.__name__=_D
_NsPlyName_Object=MibTableColumn
nsPlyName=_NsPlyName_Object((1,3,6,1,4,1,3224,10,1,1,24),_NsPlyName_Type())
nsPlyName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyName.setStatus(_A)
_NsPlyServiceName_Type=DisplayString
_NsPlyServiceName_Object=MibTableColumn
nsPlyServiceName=_NsPlyServiceName_Object((1,3,6,1,4,1,3224,10,1,1,25),_NsPlyServiceName_Type())
nsPlyServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyServiceName.setStatus(_A)
_NsPlyMonTable_Object=MibTable
nsPlyMonTable=_NsPlyMonTable_Object((1,3,6,1,4,1,3224,10,2))
if mibBuilder.loadTexts:nsPlyMonTable.setStatus(_A)
_NsPlyMonEntry_Object=MibTableRow
nsPlyMonEntry=_NsPlyMonEntry_Object((1,3,6,1,4,1,3224,10,2,1))
nsPlyMonEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:nsPlyMonEntry.setStatus(_A)
class _NsPlyMonId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsPlyMonId_Type.__name__=_C
_NsPlyMonId_Object=MibTableColumn
nsPlyMonId=_NsPlyMonId_Object((1,3,6,1,4,1,3224,10,2,1,1),_NsPlyMonId_Type())
nsPlyMonId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyMonId.setStatus(_A)
class _NsPlyMonVsys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsPlyMonVsys_Type.__name__=_C
_NsPlyMonVsys_Object=MibTableColumn
nsPlyMonVsys=_NsPlyMonVsys_Object((1,3,6,1,4,1,3224,10,2,1,2),_NsPlyMonVsys_Type())
nsPlyMonVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyMonVsys.setStatus(_A)
_NsPlyMonPackPerSec_Type=Integer32
_NsPlyMonPackPerSec_Object=MibTableColumn
nsPlyMonPackPerSec=_NsPlyMonPackPerSec_Object((1,3,6,1,4,1,3224,10,2,1,3),_NsPlyMonPackPerSec_Type())
nsPlyMonPackPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyMonPackPerSec.setStatus(_A)
_NsPlyMonPackPerMin_Type=Integer32
_NsPlyMonPackPerMin_Object=MibTableColumn
nsPlyMonPackPerMin=_NsPlyMonPackPerMin_Object((1,3,6,1,4,1,3224,10,2,1,4),_NsPlyMonPackPerMin_Type())
nsPlyMonPackPerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyMonPackPerMin.setStatus(_A)
_NsPlyMonTotalPacket_Type=Counter32
_NsPlyMonTotalPacket_Object=MibTableColumn
nsPlyMonTotalPacket=_NsPlyMonTotalPacket_Object((1,3,6,1,4,1,3224,10,2,1,5),_NsPlyMonTotalPacket_Type())
nsPlyMonTotalPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyMonTotalPacket.setStatus(_A)
_NsPlyMonBytePerSec_Type=Integer32
_NsPlyMonBytePerSec_Object=MibTableColumn
nsPlyMonBytePerSec=_NsPlyMonBytePerSec_Object((1,3,6,1,4,1,3224,10,2,1,6),_NsPlyMonBytePerSec_Type())
nsPlyMonBytePerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyMonBytePerSec.setStatus(_A)
_NsPlyMonBytePerMin_Type=Integer32
_NsPlyMonBytePerMin_Object=MibTableColumn
nsPlyMonBytePerMin=_NsPlyMonBytePerMin_Object((1,3,6,1,4,1,3224,10,2,1,7),_NsPlyMonBytePerMin_Type())
nsPlyMonBytePerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyMonBytePerMin.setStatus(_A)
_NsPlyMonTotalByte_Type=Counter32
_NsPlyMonTotalByte_Object=MibTableColumn
nsPlyMonTotalByte=_NsPlyMonTotalByte_Object((1,3,6,1,4,1,3224,10,2,1,8),_NsPlyMonTotalByte_Type())
nsPlyMonTotalByte.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyMonTotalByte.setStatus(_A)
_NsPlyMonSessionPerSec_Type=Integer32
_NsPlyMonSessionPerSec_Object=MibTableColumn
nsPlyMonSessionPerSec=_NsPlyMonSessionPerSec_Object((1,3,6,1,4,1,3224,10,2,1,9),_NsPlyMonSessionPerSec_Type())
nsPlyMonSessionPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyMonSessionPerSec.setStatus(_A)
_NsPlyMonSessionPerMin_Type=Integer32
_NsPlyMonSessionPerMin_Object=MibTableColumn
nsPlyMonSessionPerMin=_NsPlyMonSessionPerMin_Object((1,3,6,1,4,1,3224,10,2,1,10),_NsPlyMonSessionPerMin_Type())
nsPlyMonSessionPerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyMonSessionPerMin.setStatus(_A)
_NsPlyMonTotalSession_Type=Counter32
_NsPlyMonTotalSession_Object=MibTableColumn
nsPlyMonTotalSession=_NsPlyMonTotalSession_Object((1,3,6,1,4,1,3224,10,2,1,11),_NsPlyMonTotalSession_Type())
nsPlyMonTotalSession.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPlyMonTotalSession.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'netscreenPolicyMibModule':netscreenPolicyMibModule,'nsPlyTable':nsPlyTable,'nsPlyEntry':nsPlyEntry,_I:nsPlyId,_H:nsPlyVsys,'nsPlySrcZone':nsPlySrcZone,'nsPlyDstZone':nsPlyDstZone,'nsPlySrcAddr':nsPlySrcAddr,'nsPlyDstAddr':nsPlyDstAddr,'nsPlyService':nsPlyService,'nsPlyAction':nsPlyAction,'nsPlyNat':nsPlyNat,'nsPlyFixPort':nsPlyFixPort,'nsPlyDipId':nsPlyDipId,'nsPlyVpnTunnel':nsPlyVpnTunnel,'nsPlyL2tpTunnel':nsPlyL2tpTunnel,'nsPlyAuth':nsPlyAuth,'nsPlyLogEnable':nsPlyLogEnable,'nsPlyCountEnable':nsPlyCountEnable,'nsPlyAlarmBPS':nsPlyAlarmBPS,'nsPlyAlarmBPM':nsPlyAlarmBPM,'nsPlySchedule':nsPlySchedule,'nsPlyTrafficShapeEnable':nsPlyTrafficShapeEnable,'nsPlyTrafficPriority':nsPlyTrafficPriority,'nsPlyDSEnable':nsPlyDSEnable,'nsPlyActiveStatus':nsPlyActiveStatus,'nsPlyName':nsPlyName,'nsPlyServiceName':nsPlyServiceName,'nsPlyMonTable':nsPlyMonTable,'nsPlyMonEntry':nsPlyMonEntry,_J:nsPlyMonId,_K:nsPlyMonVsys,'nsPlyMonPackPerSec':nsPlyMonPackPerSec,'nsPlyMonPackPerMin':nsPlyMonPackPerMin,'nsPlyMonTotalPacket':nsPlyMonTotalPacket,'nsPlyMonBytePerSec':nsPlyMonBytePerSec,'nsPlyMonBytePerMin':nsPlyMonBytePerMin,'nsPlyMonTotalByte':nsPlyMonTotalByte,'nsPlyMonSessionPerSec':nsPlyMonSessionPerSec,'nsPlyMonSessionPerMin':nsPlyMonSessionPerMin,'nsPlyMonTotalSession':nsPlyMonTotalSession})