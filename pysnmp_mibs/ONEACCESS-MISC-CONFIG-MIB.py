_O='oacConfigBannerString'
_N='oacClockDstName'
_M='oacConfigBannerSequence'
_L='oacSntpRemoteServerAddress'
_K='oacSyslogServerAddress'
_J='seconds'
_I='oacTelnetServerBindInterfaceIndex'
_H='TruthValue'
_G='Unsigned32'
_F='Integer32'
_E='ONEACCESS-MISC-CONFIG-MIB'
_D='read-write'
_C='OctetString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
oacExpIMIpAcl,oacExpIMManagement,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMIpAcl','oacExpIMManagement','oacMIBModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention',_H)
oacMiscConfigMIB=ModuleIdentity((1,3,6,1,4,1,13191,1,100,2003))
if mibBuilder.loadTexts:oacMiscConfigMIB.setRevisions(('2011-07-26 00:00','2011-06-15 00:00','2010-12-17 00:01'))
_OacMiscConfig_ObjectIdentity=ObjectIdentity
oacMiscConfig=_OacMiscConfig_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,21))
_OacTelnetServerConfigObjects_ObjectIdentity=ObjectIdentity
oacTelnetServerConfigObjects=_OacTelnetServerConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,21,1))
_OacTelnetServerBindInterfaceTable_Object=MibTable
oacTelnetServerBindInterfaceTable=_OacTelnetServerBindInterfaceTable_Object((1,3,6,1,4,1,13191,10,3,4,21,1,1))
if mibBuilder.loadTexts:oacTelnetServerBindInterfaceTable.setStatus(_A)
_OacTelnetServerBindInterfaceEntry_Object=MibTableRow
oacTelnetServerBindInterfaceEntry=_OacTelnetServerBindInterfaceEntry_Object((1,3,6,1,4,1,13191,10,3,4,21,1,1,1))
oacTelnetServerBindInterfaceEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:oacTelnetServerBindInterfaceEntry.setStatus(_A)
_OacTelnetServerBindInterfaceIndex_Type=InterfaceIndex
_OacTelnetServerBindInterfaceIndex_Object=MibTableColumn
oacTelnetServerBindInterfaceIndex=_OacTelnetServerBindInterfaceIndex_Object((1,3,6,1,4,1,13191,10,3,4,21,1,1,1,1),_OacTelnetServerBindInterfaceIndex_Type())
oacTelnetServerBindInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oacTelnetServerBindInterfaceIndex.setStatus(_A)
class _OacTelnetServerBindInterfaceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacTelnetServerBindInterfaceName_Type.__name__=_C
_OacTelnetServerBindInterfaceName_Object=MibTableColumn
oacTelnetServerBindInterfaceName=_OacTelnetServerBindInterfaceName_Object((1,3,6,1,4,1,13191,10,3,4,21,1,1,1,2),_OacTelnetServerBindInterfaceName_Type())
oacTelnetServerBindInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:oacTelnetServerBindInterfaceName.setStatus(_A)
_OacTelnetServerBindInterfaceRowStatus_Type=RowStatus
_OacTelnetServerBindInterfaceRowStatus_Object=MibTableColumn
oacTelnetServerBindInterfaceRowStatus=_OacTelnetServerBindInterfaceRowStatus_Object((1,3,6,1,4,1,13191,10,3,4,21,1,1,1,3),_OacTelnetServerBindInterfaceRowStatus_Type())
oacTelnetServerBindInterfaceRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacTelnetServerBindInterfaceRowStatus.setStatus(_A)
class _OacTelnetServerBindAcl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacTelnetServerBindAcl_Type.__name__=_C
_OacTelnetServerBindAcl_Object=MibScalar
oacTelnetServerBindAcl=_OacTelnetServerBindAcl_Object((1,3,6,1,4,1,13191,10,3,4,21,1,2),_OacTelnetServerBindAcl_Type())
oacTelnetServerBindAcl.setMaxAccess(_D)
if mibBuilder.loadTexts:oacTelnetServerBindAcl.setStatus(_A)
class _OacTelnetServerIdleTimeout_Type(Unsigned32):defaultValue=600
_OacTelnetServerIdleTimeout_Type.__name__=_G
_OacTelnetServerIdleTimeout_Object=MibScalar
oacTelnetServerIdleTimeout=_OacTelnetServerIdleTimeout_Object((1,3,6,1,4,1,13191,10,3,4,21,1,3),_OacTelnetServerIdleTimeout_Type())
oacTelnetServerIdleTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:oacTelnetServerIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:oacTelnetServerIdleTimeout.setUnits(_J)
class _OacTelnetServerLogEnable_Type(TruthValue):defaultValue=1
_OacTelnetServerLogEnable_Type.__name__=_H
_OacTelnetServerLogEnable_Object=MibScalar
oacTelnetServerLogEnable=_OacTelnetServerLogEnable_Object((1,3,6,1,4,1,13191,10,3,4,21,1,4),_OacTelnetServerLogEnable_Type())
oacTelnetServerLogEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:oacTelnetServerLogEnable.setStatus(_A)
class _OacTelnetServerLogFileSize_Type(Integer32):defaultValue=8200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(82,8200))
_OacTelnetServerLogFileSize_Type.__name__=_F
_OacTelnetServerLogFileSize_Object=MibScalar
oacTelnetServerLogFileSize=_OacTelnetServerLogFileSize_Object((1,3,6,1,4,1,13191,10,3,4,21,1,5),_OacTelnetServerLogFileSize_Type())
oacTelnetServerLogFileSize.setMaxAccess(_D)
if mibBuilder.loadTexts:oacTelnetServerLogFileSize.setStatus(_A)
if mibBuilder.loadTexts:oacTelnetServerLogFileSize.setUnits('bytes')
_OacSyslogServerConfigObjects_ObjectIdentity=ObjectIdentity
oacSyslogServerConfigObjects=_OacSyslogServerConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,21,2))
_OacSyslogServerTable_Object=MibTable
oacSyslogServerTable=_OacSyslogServerTable_Object((1,3,6,1,4,1,13191,10,3,4,21,2,1))
if mibBuilder.loadTexts:oacSyslogServerTable.setStatus(_A)
_OacSyslogServerEntry_Object=MibTableRow
oacSyslogServerEntry=_OacSyslogServerEntry_Object((1,3,6,1,4,1,13191,10,3,4,21,2,1,1))
oacSyslogServerEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:oacSyslogServerEntry.setStatus(_A)
class _OacSyslogServerAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacSyslogServerAddress_Type.__name__=_C
_OacSyslogServerAddress_Object=MibTableColumn
oacSyslogServerAddress=_OacSyslogServerAddress_Object((1,3,6,1,4,1,13191,10,3,4,21,2,1,1,1),_OacSyslogServerAddress_Type())
oacSyslogServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSyslogServerAddress.setStatus(_A)
class _OacSyslogServerFacilityNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_OacSyslogServerFacilityNum_Type.__name__=_F
_OacSyslogServerFacilityNum_Object=MibTableColumn
oacSyslogServerFacilityNum=_OacSyslogServerFacilityNum_Object((1,3,6,1,4,1,13191,10,3,4,21,2,1,1,2),_OacSyslogServerFacilityNum_Type())
oacSyslogServerFacilityNum.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSyslogServerFacilityNum.setStatus(_A)
_OacSyslogServerInterface_Type=InterfaceIndex
_OacSyslogServerInterface_Object=MibTableColumn
oacSyslogServerInterface=_OacSyslogServerInterface_Object((1,3,6,1,4,1,13191,10,3,4,21,2,1,1,3),_OacSyslogServerInterface_Type())
oacSyslogServerInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSyslogServerInterface.setStatus(_A)
_OacSyslogServerRowStatus_Type=RowStatus
_OacSyslogServerRowStatus_Object=MibTableColumn
oacSyslogServerRowStatus=_OacSyslogServerRowStatus_Object((1,3,6,1,4,1,13191,10,3,4,21,2,1,1,4),_OacSyslogServerRowStatus_Type())
oacSyslogServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSyslogServerRowStatus.setStatus(_A)
class _OacSyslogMaxServers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_OacSyslogMaxServers_Type.__name__=_F
_OacSyslogMaxServers_Object=MibScalar
oacSyslogMaxServers=_OacSyslogMaxServers_Object((1,3,6,1,4,1,13191,10,3,4,21,2,2),_OacSyslogMaxServers_Type())
oacSyslogMaxServers.setMaxAccess(_D)
if mibBuilder.loadTexts:oacSyslogMaxServers.setStatus(_A)
_OacSntpClientConfigObjects_ObjectIdentity=ObjectIdentity
oacSntpClientConfigObjects=_OacSntpClientConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,21,3))
_OacSntpClientBroadcastEnable_Type=TruthValue
_OacSntpClientBroadcastEnable_Object=MibScalar
oacSntpClientBroadcastEnable=_OacSntpClientBroadcastEnable_Object((1,3,6,1,4,1,13191,10,3,4,21,3,1),_OacSntpClientBroadcastEnable_Type())
oacSntpClientBroadcastEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:oacSntpClientBroadcastEnable.setStatus(_A)
_OacSntpRemoteServerTable_Object=MibTable
oacSntpRemoteServerTable=_OacSntpRemoteServerTable_Object((1,3,6,1,4,1,13191,10,3,4,21,3,2))
if mibBuilder.loadTexts:oacSntpRemoteServerTable.setStatus(_A)
_OacSntpRemoteServerEntry_Object=MibTableRow
oacSntpRemoteServerEntry=_OacSntpRemoteServerEntry_Object((1,3,6,1,4,1,13191,10,3,4,21,3,2,1))
oacSntpRemoteServerEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:oacSntpRemoteServerEntry.setStatus(_A)
class _OacSntpRemoteServerAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacSntpRemoteServerAddress_Type.__name__=_C
_OacSntpRemoteServerAddress_Object=MibTableColumn
oacSntpRemoteServerAddress=_OacSntpRemoteServerAddress_Object((1,3,6,1,4,1,13191,10,3,4,21,3,2,1,1),_OacSntpRemoteServerAddress_Type())
oacSntpRemoteServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSntpRemoteServerAddress.setStatus(_A)
_OacSntpRemoteServerInterface_Type=InterfaceIndex
_OacSntpRemoteServerInterface_Object=MibTableColumn
oacSntpRemoteServerInterface=_OacSntpRemoteServerInterface_Object((1,3,6,1,4,1,13191,10,3,4,21,3,2,1,2),_OacSntpRemoteServerInterface_Type())
oacSntpRemoteServerInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSntpRemoteServerInterface.setStatus(_A)
_OacSntpRemoteServerRowStatus_Type=RowStatus
_OacSntpRemoteServerRowStatus_Object=MibTableColumn
oacSntpRemoteServerRowStatus=_OacSntpRemoteServerRowStatus_Object((1,3,6,1,4,1,13191,10,3,4,21,3,2,1,3),_OacSntpRemoteServerRowStatus_Type())
oacSntpRemoteServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSntpRemoteServerRowStatus.setStatus(_A)
class _OacSntpClientPollInterval_Type(Unsigned32):defaultValue=64
_OacSntpClientPollInterval_Type.__name__=_G
_OacSntpClientPollInterval_Object=MibScalar
oacSntpClientPollInterval=_OacSntpClientPollInterval_Object((1,3,6,1,4,1,13191,10,3,4,21,3,3),_OacSntpClientPollInterval_Type())
oacSntpClientPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:oacSntpClientPollInterval.setStatus(_A)
if mibBuilder.loadTexts:oacSntpClientPollInterval.setUnits(_J)
_OacBannerConfigObjects_ObjectIdentity=ObjectIdentity
oacBannerConfigObjects=_OacBannerConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,21,4))
_OacConfigBannerSeqTable_Object=MibTable
oacConfigBannerSeqTable=_OacConfigBannerSeqTable_Object((1,3,6,1,4,1,13191,10,3,4,21,4,1))
if mibBuilder.loadTexts:oacConfigBannerSeqTable.setStatus(_A)
_OacConfigBannerSeqEntry_Object=MibTableRow
oacConfigBannerSeqEntry=_OacConfigBannerSeqEntry_Object((1,3,6,1,4,1,13191,10,3,4,21,4,1,1))
oacConfigBannerSeqEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:oacConfigBannerSeqEntry.setStatus(_A)
class _OacConfigBannerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('motd',1),('exec',2)))
_OacConfigBannerType_Type.__name__=_F
_OacConfigBannerType_Object=MibTableColumn
oacConfigBannerType=_OacConfigBannerType_Object((1,3,6,1,4,1,13191,10,3,4,21,4,1,1,1),_OacConfigBannerType_Type())
oacConfigBannerType.setMaxAccess(_B)
if mibBuilder.loadTexts:oacConfigBannerType.setStatus(_A)
class _OacConfigBannerSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_OacConfigBannerSequence_Type.__name__=_F
_OacConfigBannerSequence_Object=MibTableColumn
oacConfigBannerSequence=_OacConfigBannerSequence_Object((1,3,6,1,4,1,13191,10,3,4,21,4,1,1,2),_OacConfigBannerSequence_Type())
oacConfigBannerSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:oacConfigBannerSequence.setStatus(_A)
class _OacConfigBannerString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacConfigBannerString_Type.__name__=_C
_OacConfigBannerString_Object=MibTableColumn
oacConfigBannerString=_OacConfigBannerString_Object((1,3,6,1,4,1,13191,10,3,4,21,4,1,1,3),_OacConfigBannerString_Type())
oacConfigBannerString.setMaxAccess(_B)
if mibBuilder.loadTexts:oacConfigBannerString.setStatus(_A)
_OacConfigBannerSeqRowStatus_Type=RowStatus
_OacConfigBannerSeqRowStatus_Object=MibTableColumn
oacConfigBannerSeqRowStatus=_OacConfigBannerSeqRowStatus_Object((1,3,6,1,4,1,13191,10,3,4,21,4,1,1,4),_OacConfigBannerSeqRowStatus_Type())
oacConfigBannerSeqRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacConfigBannerSeqRowStatus.setStatus(_A)
class _OacConfigMotdBanner_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,230))
_OacConfigMotdBanner_Type.__name__=_C
_OacConfigMotdBanner_Object=MibScalar
oacConfigMotdBanner=_OacConfigMotdBanner_Object((1,3,6,1,4,1,13191,10,3,4,21,4,2),_OacConfigMotdBanner_Type())
oacConfigMotdBanner.setMaxAccess(_D)
if mibBuilder.loadTexts:oacConfigMotdBanner.setStatus(_A)
class _OacConfigExecBanner_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,230))
_OacConfigExecBanner_Type.__name__=_C
_OacConfigExecBanner_Object=MibScalar
oacConfigExecBanner=_OacConfigExecBanner_Object((1,3,6,1,4,1,13191,10,3,4,21,4,3),_OacConfigExecBanner_Type())
oacConfigExecBanner.setMaxAccess(_D)
if mibBuilder.loadTexts:oacConfigExecBanner.setStatus(_A)
_OacDateAndTimeConfigObjects_ObjectIdentity=ObjectIdentity
oacDateAndTimeConfigObjects=_OacDateAndTimeConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,21,5))
_OacMiscConfigDateAndTime_Type=DateAndTime
_OacMiscConfigDateAndTime_Object=MibScalar
oacMiscConfigDateAndTime=_OacMiscConfigDateAndTime_Object((1,3,6,1,4,1,13191,10,3,4,21,5,1),_OacMiscConfigDateAndTime_Type())
oacMiscConfigDateAndTime.setMaxAccess(_D)
if mibBuilder.loadTexts:oacMiscConfigDateAndTime.setStatus(_A)
_OacConfigClockDstTable_Object=MibTable
oacConfigClockDstTable=_OacConfigClockDstTable_Object((1,3,6,1,4,1,13191,10,3,4,21,5,2))
if mibBuilder.loadTexts:oacConfigClockDstTable.setStatus(_A)
_OacConfigClockDstEntry_Object=MibTableRow
oacConfigClockDstEntry=_OacConfigClockDstEntry_Object((1,3,6,1,4,1,13191,10,3,4,21,5,2,1))
oacConfigClockDstEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:oacConfigClockDstEntry.setStatus(_A)
class _OacClockDstName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacClockDstName_Type.__name__=_C
_OacClockDstName_Object=MibTableColumn
oacClockDstName=_OacClockDstName_Object((1,3,6,1,4,1,13191,10,3,4,21,5,2,1,1),_OacClockDstName_Type())
oacClockDstName.setMaxAccess(_B)
if mibBuilder.loadTexts:oacClockDstName.setStatus(_A)
class _OacClockDstSummerStartWeek_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacClockDstSummerStartWeek_Type.__name__=_C
_OacClockDstSummerStartWeek_Object=MibTableColumn
oacClockDstSummerStartWeek=_OacClockDstSummerStartWeek_Object((1,3,6,1,4,1,13191,10,3,4,21,5,2,1,2),_OacClockDstSummerStartWeek_Type())
oacClockDstSummerStartWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:oacClockDstSummerStartWeek.setStatus(_A)
class _OacClockDstSummerStartDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacClockDstSummerStartDate_Type.__name__=_C
_OacClockDstSummerStartDate_Object=MibTableColumn
oacClockDstSummerStartDate=_OacClockDstSummerStartDate_Object((1,3,6,1,4,1,13191,10,3,4,21,5,2,1,3),_OacClockDstSummerStartDate_Type())
oacClockDstSummerStartDate.setMaxAccess(_B)
if mibBuilder.loadTexts:oacClockDstSummerStartDate.setStatus(_A)
class _OacClockDstWinterStartWeek_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacClockDstWinterStartWeek_Type.__name__=_C
_OacClockDstWinterStartWeek_Object=MibTableColumn
oacClockDstWinterStartWeek=_OacClockDstWinterStartWeek_Object((1,3,6,1,4,1,13191,10,3,4,21,5,2,1,4),_OacClockDstWinterStartWeek_Type())
oacClockDstWinterStartWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:oacClockDstWinterStartWeek.setStatus(_A)
class _OacClockDstWinterStartDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacClockDstWinterStartDate_Type.__name__=_C
_OacClockDstWinterStartDate_Object=MibTableColumn
oacClockDstWinterStartDate=_OacClockDstWinterStartDate_Object((1,3,6,1,4,1,13191,10,3,4,21,5,2,1,5),_OacClockDstWinterStartDate_Type())
oacClockDstWinterStartDate.setMaxAccess(_B)
if mibBuilder.loadTexts:oacClockDstWinterStartDate.setStatus(_A)
_OacClockDstRowStatus_Type=RowStatus
_OacClockDstRowStatus_Object=MibTableColumn
oacClockDstRowStatus=_OacClockDstRowStatus_Object((1,3,6,1,4,1,13191,10,3,4,21,5,2,1,6),_OacClockDstRowStatus_Type())
oacClockDstRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacClockDstRowStatus.setStatus(_A)
_OacMiscConfigConformance_ObjectIdentity=ObjectIdentity
oacMiscConfigConformance=_OacMiscConfigConformance_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,21,6))
_OacMiscConfigGroups_ObjectIdentity=ObjectIdentity
oacMiscConfigGroups=_OacMiscConfigGroups_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,21,6,1))
_OacMiscCompls_ObjectIdentity=ObjectIdentity
oacMiscCompls=_OacMiscCompls_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,21,6,2))
oacMiscConfigGroup=ObjectGroup((1,3,6,1,4,1,13191,10,3,4,21,6,1,1))
oacMiscConfigGroup.setObjects((_E,_O))
if mibBuilder.loadTexts:oacMiscConfigGroup.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'oacMiscConfigMIB':oacMiscConfigMIB,'oacMiscConfig':oacMiscConfig,'oacTelnetServerConfigObjects':oacTelnetServerConfigObjects,'oacTelnetServerBindInterfaceTable':oacTelnetServerBindInterfaceTable,'oacTelnetServerBindInterfaceEntry':oacTelnetServerBindInterfaceEntry,_I:oacTelnetServerBindInterfaceIndex,'oacTelnetServerBindInterfaceName':oacTelnetServerBindInterfaceName,'oacTelnetServerBindInterfaceRowStatus':oacTelnetServerBindInterfaceRowStatus,'oacTelnetServerBindAcl':oacTelnetServerBindAcl,'oacTelnetServerIdleTimeout':oacTelnetServerIdleTimeout,'oacTelnetServerLogEnable':oacTelnetServerLogEnable,'oacTelnetServerLogFileSize':oacTelnetServerLogFileSize,'oacSyslogServerConfigObjects':oacSyslogServerConfigObjects,'oacSyslogServerTable':oacSyslogServerTable,'oacSyslogServerEntry':oacSyslogServerEntry,_K:oacSyslogServerAddress,'oacSyslogServerFacilityNum':oacSyslogServerFacilityNum,'oacSyslogServerInterface':oacSyslogServerInterface,'oacSyslogServerRowStatus':oacSyslogServerRowStatus,'oacSyslogMaxServers':oacSyslogMaxServers,'oacSntpClientConfigObjects':oacSntpClientConfigObjects,'oacSntpClientBroadcastEnable':oacSntpClientBroadcastEnable,'oacSntpRemoteServerTable':oacSntpRemoteServerTable,'oacSntpRemoteServerEntry':oacSntpRemoteServerEntry,_L:oacSntpRemoteServerAddress,'oacSntpRemoteServerInterface':oacSntpRemoteServerInterface,'oacSntpRemoteServerRowStatus':oacSntpRemoteServerRowStatus,'oacSntpClientPollInterval':oacSntpClientPollInterval,'oacBannerConfigObjects':oacBannerConfigObjects,'oacConfigBannerSeqTable':oacConfigBannerSeqTable,'oacConfigBannerSeqEntry':oacConfigBannerSeqEntry,'oacConfigBannerType':oacConfigBannerType,_M:oacConfigBannerSequence,_O:oacConfigBannerString,'oacConfigBannerSeqRowStatus':oacConfigBannerSeqRowStatus,'oacConfigMotdBanner':oacConfigMotdBanner,'oacConfigExecBanner':oacConfigExecBanner,'oacDateAndTimeConfigObjects':oacDateAndTimeConfigObjects,'oacMiscConfigDateAndTime':oacMiscConfigDateAndTime,'oacConfigClockDstTable':oacConfigClockDstTable,'oacConfigClockDstEntry':oacConfigClockDstEntry,_N:oacClockDstName,'oacClockDstSummerStartWeek':oacClockDstSummerStartWeek,'oacClockDstSummerStartDate':oacClockDstSummerStartDate,'oacClockDstWinterStartWeek':oacClockDstWinterStartWeek,'oacClockDstWinterStartDate':oacClockDstWinterStartDate,'oacClockDstRowStatus':oacClockDstRowStatus,'oacMiscConfigConformance':oacMiscConfigConformance,'oacMiscConfigGroups':oacMiscConfigGroups,'oacMiscConfigGroup':oacMiscConfigGroup,'oacMiscCompls':oacMiscCompls})