_AG='fsaJobObjectGroup'
_AF='fsaSoftwareObjectGroup'
_AE='fsaSystemObjectGroup'
_AD='fsaNotificationGroup'
_AC='fsaTrapCntExp'
_AB='fsaTrapLKDN'
_AA='fsaTrapLKUP'
_A9='fsaTrapAST'
_A8='fsaTrapRDM'
_A7='fsaTrapHCH'
_A6='fsaTrapHCT'
_A5='fsaTrapPSUC'
_A4='fsaTrapDUHigh'
_A3='fsaTrapMemHigh'
_A2='fsaTrapCPUHigh'
_A1='fsaTrapMalware'
_A0='fsaTrapContractExpire'
_z='fsaTrapLinkDown'
_y='fsaTrapLinkUp'
_x='fsaTrapAvgScanTime'
_w='fsaTrapRaidMsg'
_v='fsaTrapHCHealth'
_u='fsaTrapHCTopology'
_t='fsaTrapPSUFailure'
_s='fsaTrapDUrate'
_r='fsaTrapMUrate'
_q='fsaTrapCPUrate'
_p='fsaTrapJobInfo'
_o='fsaJobProcessing'
_n='fsaFTypePre'
_m='fsaFTypeNOVM'
_l='fsaFTypeExtra'
_k='fsaFTypeURL'
_j='fsaFTypeMAC'
_i='fsaFTypeAndroid'
_h='fsaFTypeWEB'
_g='fsaFTypeFLASH'
_f='fsaFTypeDOC'
_e='fsaFTypePDF'
_d='fsaFTypeExe'
_c='fsaFwUserState'
_b='fsaFwUserAuth'
_a='fsaFwUserName'
_Z='fsaFwUserAuthTimeout'
_Y='fsaFwUserNumber'
_X='fsaSysIPS'
_W='fsaSysSniffer'
_V='fsaSysTool'
_U='fsaSysRating'
_T='fsaSysTracer'
_S='fsaSysUpTime'
_R='fsaSysCpuUsageExcludedNice'
_Q='fsaSysDiskCapacity'
_P='fsaSysDiskUsage'
_O='fsaSysMemCapacity'
_N='fsaSysMemUsage'
_M='fsaSysCpuUsage'
_L='fsaSysVersion'
_K='fsaFwUserIndex'
_J='Gauge32'
_I='DisplayString'
_H='accessible-for-notify'
_G='sysName'
_F='SNMPv2-MIB'
_E='fnSysSerial'
_D='FORTINET-CORE-MIB'
_C='read-only'
_B='FORTINET-FORTISANDBOX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FnBoolState,FnIndex,fnAdminEntry,fnSysSerial,fortinet=mibBuilder.importSymbols(_D,'FnBoolState','FnIndex','fnAdminEntry',_E,'fortinet')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ifEntry,ifName=mibBuilder.importSymbols('IF-MIB','ifEntry','ifName')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_F,_G)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_J,'Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_I,'PhysAddress','TextualConvention')
fnFortiSandboxMib=ModuleIdentity((1,3,6,1,4,1,12356,118))
if mibBuilder.loadTexts:fnFortiSandboxMib.setRevisions(('2014-02-24 00:00',))
class FsaAdminPermLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,15,255)));namedValues=NamedValues(*(('readAdmin',0),('writeAdmin',1),('domainAdmin',15),('superAdmin',255)))
class FsaUserAuthType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),('radiusSingle',2),('radiusMultiple',3),('ldap',4)))
class FsaSessProto(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6,8,12,17,22,41,46,47,50,51,89,103,108,255)));namedValues=NamedValues(*(('ip',0),('icmp',1),('igmp',2),('ipip',4),('tcp',6),('egp',8),('pup',12),('udp',17),('idp',22),('ipv6',41),('rsvp',46),('gre',47),('esp',50),('ah',51),('ospf',89),('pim',103),('comp',108),('raw',255)))
_FsaModel_ObjectIdentity=ObjectIdentity
fsaModel=_FsaModel_ObjectIdentity((1,3,6,1,4,1,12356,118,1))
_Fsa1000D_ObjectIdentity=ObjectIdentity
fsa1000D=_Fsa1000D_ObjectIdentity((1,3,6,1,4,1,12356,118,1,10004))
_FsaVM_ObjectIdentity=ObjectIdentity
fsaVM=_FsaVM_ObjectIdentity((1,3,6,1,4,1,12356,118,1,20000))
_Fsa3000D_ObjectIdentity=ObjectIdentity
fsa3000D=_Fsa3000D_ObjectIdentity((1,3,6,1,4,1,12356,118,1,30004))
_Fsa3500D_ObjectIdentity=ObjectIdentity
fsa3500D=_Fsa3500D_ObjectIdentity((1,3,6,1,4,1,12356,118,1,30005))
_Fsa3000E_ObjectIdentity=ObjectIdentity
fsa3000E=_Fsa3000E_ObjectIdentity((1,3,6,1,4,1,12356,118,1,30006))
_Fsa2000E_ObjectIdentity=ObjectIdentity
fsa2000E=_Fsa2000E_ObjectIdentity((1,3,6,1,4,1,12356,118,1,30007))
_Fsa1000F_ObjectIdentity=ObjectIdentity
fsa1000F=_Fsa1000F_ObjectIdentity((1,3,6,1,4,1,12356,118,1,30008))
_Fsa500F_ObjectIdentity=ObjectIdentity
fsa500F=_Fsa500F_ObjectIdentity((1,3,6,1,4,1,12356,118,1,30009))
_Fsa3000F_ObjectIdentity=ObjectIdentity
fsa3000F=_Fsa3000F_ObjectIdentity((1,3,6,1,4,1,12356,118,1,30010))
_Fsa1000FDC_ObjectIdentity=ObjectIdentity
fsa1000FDC=_Fsa1000FDC_ObjectIdentity((1,3,6,1,4,1,12356,118,1,30011))
_FsaTraps_ObjectIdentity=ObjectIdentity
fsaTraps=_FsaTraps_ObjectIdentity((1,3,6,1,4,1,12356,118,2))
_FsaTrapPrefix_ObjectIdentity=ObjectIdentity
fsaTrapPrefix=_FsaTrapPrefix_ObjectIdentity((1,3,6,1,4,1,12356,118,2,0))
_FsaSystem_ObjectIdentity=ObjectIdentity
fsaSystem=_FsaSystem_ObjectIdentity((1,3,6,1,4,1,12356,118,3))
_FsaSystemInfo_ObjectIdentity=ObjectIdentity
fsaSystemInfo=_FsaSystemInfo_ObjectIdentity((1,3,6,1,4,1,12356,118,3,1))
class _FsaSysVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsaSysVersion_Type.__name__=_I
_FsaSysVersion_Object=MibScalar
fsaSysVersion=_FsaSysVersion_Object((1,3,6,1,4,1,12356,118,3,1,1),_FsaSysVersion_Type())
fsaSysVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaSysVersion.setStatus(_A)
class _FsaSysCpuUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsaSysCpuUsage_Type.__name__=_J
_FsaSysCpuUsage_Object=MibScalar
fsaSysCpuUsage=_FsaSysCpuUsage_Object((1,3,6,1,4,1,12356,118,3,1,2),_FsaSysCpuUsage_Type())
fsaSysCpuUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaSysCpuUsage.setStatus(_A)
class _FsaSysMemUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsaSysMemUsage_Type.__name__=_J
_FsaSysMemUsage_Object=MibScalar
fsaSysMemUsage=_FsaSysMemUsage_Object((1,3,6,1,4,1,12356,118,3,1,3),_FsaSysMemUsage_Type())
fsaSysMemUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaSysMemUsage.setStatus(_A)
_FsaSysMemCapacity_Type=Gauge32
_FsaSysMemCapacity_Object=MibScalar
fsaSysMemCapacity=_FsaSysMemCapacity_Object((1,3,6,1,4,1,12356,118,3,1,4),_FsaSysMemCapacity_Type())
fsaSysMemCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaSysMemCapacity.setStatus(_A)
_FsaSysDiskUsage_Type=Gauge32
_FsaSysDiskUsage_Object=MibScalar
fsaSysDiskUsage=_FsaSysDiskUsage_Object((1,3,6,1,4,1,12356,118,3,1,5),_FsaSysDiskUsage_Type())
fsaSysDiskUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaSysDiskUsage.setStatus(_A)
_FsaSysDiskCapacity_Type=Gauge32
_FsaSysDiskCapacity_Object=MibScalar
fsaSysDiskCapacity=_FsaSysDiskCapacity_Object((1,3,6,1,4,1,12356,118,3,1,6),_FsaSysDiskCapacity_Type())
fsaSysDiskCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaSysDiskCapacity.setStatus(_A)
class _FsaSysCpuUsageExcludedNice_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsaSysCpuUsageExcludedNice_Type.__name__=_J
_FsaSysCpuUsageExcludedNice_Object=MibScalar
fsaSysCpuUsageExcludedNice=_FsaSysCpuUsageExcludedNice_Object((1,3,6,1,4,1,12356,118,3,1,7),_FsaSysCpuUsageExcludedNice_Type())
fsaSysCpuUsageExcludedNice.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaSysCpuUsageExcludedNice.setStatus(_A)
_FsaSysUpTime_Type=Counter64
_FsaSysUpTime_Object=MibScalar
fsaSysUpTime=_FsaSysUpTime_Object((1,3,6,1,4,1,12356,118,3,1,8),_FsaSysUpTime_Type())
fsaSysUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaSysUpTime.setStatus(_A)
if mibBuilder.loadTexts:fsaSysUpTime.setUnits('hundredths of a second')
_FsaSoftware_ObjectIdentity=ObjectIdentity
fsaSoftware=_FsaSoftware_ObjectIdentity((1,3,6,1,4,1,12356,118,3,2))
class _FsaSysTracer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsaSysTracer_Type.__name__=_I
_FsaSysTracer_Object=MibScalar
fsaSysTracer=_FsaSysTracer_Object((1,3,6,1,4,1,12356,118,3,2,1),_FsaSysTracer_Type())
fsaSysTracer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaSysTracer.setStatus(_A)
class _FsaSysRating_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsaSysRating_Type.__name__=_I
_FsaSysRating_Object=MibScalar
fsaSysRating=_FsaSysRating_Object((1,3,6,1,4,1,12356,118,3,2,2),_FsaSysRating_Type())
fsaSysRating.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaSysRating.setStatus(_A)
class _FsaSysTool_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsaSysTool_Type.__name__=_I
_FsaSysTool_Object=MibScalar
fsaSysTool=_FsaSysTool_Object((1,3,6,1,4,1,12356,118,3,2,3),_FsaSysTool_Type())
fsaSysTool.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaSysTool.setStatus(_A)
class _FsaSysSniffer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsaSysSniffer_Type.__name__=_I
_FsaSysSniffer_Object=MibScalar
fsaSysSniffer=_FsaSysSniffer_Object((1,3,6,1,4,1,12356,118,3,2,4),_FsaSysSniffer_Type())
fsaSysSniffer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaSysSniffer.setStatus(_A)
class _FsaSysIPS_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsaSysIPS_Type.__name__=_I
_FsaSysIPS_Object=MibScalar
fsaSysIPS=_FsaSysIPS_Object((1,3,6,1,4,1,12356,118,3,2,5),_FsaSysIPS_Type())
fsaSysIPS.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaSysIPS.setStatus(_A)
_FsaFwUsers_ObjectIdentity=ObjectIdentity
fsaFwUsers=_FsaFwUsers_ObjectIdentity((1,3,6,1,4,1,12356,118,4))
_FsaFwUserInfo_ObjectIdentity=ObjectIdentity
fsaFwUserInfo=_FsaFwUserInfo_ObjectIdentity((1,3,6,1,4,1,12356,118,4,1))
_FsaFwUserNumber_Type=Integer32
_FsaFwUserNumber_Object=MibScalar
fsaFwUserNumber=_FsaFwUserNumber_Object((1,3,6,1,4,1,12356,118,4,1,1),_FsaFwUserNumber_Type())
fsaFwUserNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFwUserNumber.setStatus(_A)
_FsaFwUserAuthTimeout_Type=Integer32
_FsaFwUserAuthTimeout_Object=MibScalar
fsaFwUserAuthTimeout=_FsaFwUserAuthTimeout_Object((1,3,6,1,4,1,12356,118,4,1,2),_FsaFwUserAuthTimeout_Type())
fsaFwUserAuthTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFwUserAuthTimeout.setStatus(_A)
_FsaFwUserTables_ObjectIdentity=ObjectIdentity
fsaFwUserTables=_FsaFwUserTables_ObjectIdentity((1,3,6,1,4,1,12356,118,4,2))
_FsaFwUserTable_Object=MibTable
fsaFwUserTable=_FsaFwUserTable_Object((1,3,6,1,4,1,12356,118,4,2,1))
if mibBuilder.loadTexts:fsaFwUserTable.setStatus(_A)
_FsaFwUserEntry_Object=MibTableRow
fsaFwUserEntry=_FsaFwUserEntry_Object((1,3,6,1,4,1,12356,118,4,2,1,1))
fsaFwUserEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:fsaFwUserEntry.setStatus(_A)
_FsaFwUserIndex_Type=FnIndex
_FsaFwUserIndex_Object=MibTableColumn
fsaFwUserIndex=_FsaFwUserIndex_Object((1,3,6,1,4,1,12356,118,4,2,1,1,1),_FsaFwUserIndex_Type())
fsaFwUserIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsaFwUserIndex.setStatus(_A)
_FsaFwUserName_Type=DisplayString
_FsaFwUserName_Object=MibTableColumn
fsaFwUserName=_FsaFwUserName_Object((1,3,6,1,4,1,12356,118,4,2,1,1,2),_FsaFwUserName_Type())
fsaFwUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFwUserName.setStatus(_A)
_FsaFwUserAuth_Type=FsaUserAuthType
_FsaFwUserAuth_Object=MibTableColumn
fsaFwUserAuth=_FsaFwUserAuth_Object((1,3,6,1,4,1,12356,118,4,2,1,1,3),_FsaFwUserAuth_Type())
fsaFwUserAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFwUserAuth.setStatus(_A)
_FsaFwUserState_Type=FnBoolState
_FsaFwUserState_Object=MibTableColumn
fsaFwUserState=_FsaFwUserState_Object((1,3,6,1,4,1,12356,118,4,2,1,1,4),_FsaFwUserState_Type())
fsaFwUserState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFwUserState.setStatus(_A)
_FsaJobInfo_ObjectIdentity=ObjectIdentity
fsaJobInfo=_FsaJobInfo_ObjectIdentity((1,3,6,1,4,1,12356,118,5))
_FsaJobQueue_ObjectIdentity=ObjectIdentity
fsaJobQueue=_FsaJobQueue_ObjectIdentity((1,3,6,1,4,1,12356,118,5,1))
_FsaFTypeExe_Type=Integer32
_FsaFTypeExe_Object=MibScalar
fsaFTypeExe=_FsaFTypeExe_Object((1,3,6,1,4,1,12356,118,5,1,1),_FsaFTypeExe_Type())
fsaFTypeExe.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFTypeExe.setStatus(_A)
_FsaFTypePDF_Type=Integer32
_FsaFTypePDF_Object=MibScalar
fsaFTypePDF=_FsaFTypePDF_Object((1,3,6,1,4,1,12356,118,5,1,2),_FsaFTypePDF_Type())
fsaFTypePDF.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFTypePDF.setStatus(_A)
_FsaFTypeDOC_Type=Integer32
_FsaFTypeDOC_Object=MibScalar
fsaFTypeDOC=_FsaFTypeDOC_Object((1,3,6,1,4,1,12356,118,5,1,3),_FsaFTypeDOC_Type())
fsaFTypeDOC.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFTypeDOC.setStatus(_A)
_FsaFTypeFLASH_Type=Integer32
_FsaFTypeFLASH_Object=MibScalar
fsaFTypeFLASH=_FsaFTypeFLASH_Object((1,3,6,1,4,1,12356,118,5,1,4),_FsaFTypeFLASH_Type())
fsaFTypeFLASH.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFTypeFLASH.setStatus(_A)
_FsaFTypeWEB_Type=Integer32
_FsaFTypeWEB_Object=MibScalar
fsaFTypeWEB=_FsaFTypeWEB_Object((1,3,6,1,4,1,12356,118,5,1,5),_FsaFTypeWEB_Type())
fsaFTypeWEB.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFTypeWEB.setStatus(_A)
_FsaFTypeAndroid_Type=Integer32
_FsaFTypeAndroid_Object=MibScalar
fsaFTypeAndroid=_FsaFTypeAndroid_Object((1,3,6,1,4,1,12356,118,5,1,6),_FsaFTypeAndroid_Type())
fsaFTypeAndroid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFTypeAndroid.setStatus(_A)
_FsaFTypeMAC_Type=Integer32
_FsaFTypeMAC_Object=MibScalar
fsaFTypeMAC=_FsaFTypeMAC_Object((1,3,6,1,4,1,12356,118,5,1,7),_FsaFTypeMAC_Type())
fsaFTypeMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFTypeMAC.setStatus(_A)
_FsaFTypeURL_Type=Integer32
_FsaFTypeURL_Object=MibScalar
fsaFTypeURL=_FsaFTypeURL_Object((1,3,6,1,4,1,12356,118,5,1,8),_FsaFTypeURL_Type())
fsaFTypeURL.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFTypeURL.setStatus(_A)
_FsaFTypeExtra_Type=Integer32
_FsaFTypeExtra_Object=MibScalar
fsaFTypeExtra=_FsaFTypeExtra_Object((1,3,6,1,4,1,12356,118,5,1,9),_FsaFTypeExtra_Type())
fsaFTypeExtra.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFTypeExtra.setStatus(_A)
_FsaFTypeNOVM_Type=Integer32
_FsaFTypeNOVM_Object=MibScalar
fsaFTypeNOVM=_FsaFTypeNOVM_Object((1,3,6,1,4,1,12356,118,5,1,10),_FsaFTypeNOVM_Type())
fsaFTypeNOVM.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFTypeNOVM.setStatus(_A)
_FsaFTypePre_Type=Integer32
_FsaFTypePre_Object=MibScalar
fsaFTypePre=_FsaFTypePre_Object((1,3,6,1,4,1,12356,118,5,1,11),_FsaFTypePre_Type())
fsaFTypePre.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaFTypePre.setStatus(_A)
_FsaJobProcessing_Type=Integer32
_FsaJobProcessing_Object=MibScalar
fsaJobProcessing=_FsaJobProcessing_Object((1,3,6,1,4,1,12356,118,5,1,12),_FsaJobProcessing_Type())
fsaJobProcessing.setMaxAccess(_C)
if mibBuilder.loadTexts:fsaJobProcessing.setStatus(_A)
_FsaTrapObjects_ObjectIdentity=ObjectIdentity
fsaTrapObjects=_FsaTrapObjects_ObjectIdentity((1,3,6,1,4,1,12356,118,6))
_FsaTrapJobInfo_Type=DisplayString
_FsaTrapJobInfo_Object=MibScalar
fsaTrapJobInfo=_FsaTrapJobInfo_Object((1,3,6,1,4,1,12356,118,6,1),_FsaTrapJobInfo_Type())
fsaTrapJobInfo.setMaxAccess(_H)
if mibBuilder.loadTexts:fsaTrapJobInfo.setStatus(_A)
_FsaTrapCPUrate_Type=DisplayString
_FsaTrapCPUrate_Object=MibScalar
fsaTrapCPUrate=_FsaTrapCPUrate_Object((1,3,6,1,4,1,12356,118,6,2),_FsaTrapCPUrate_Type())
fsaTrapCPUrate.setMaxAccess(_H)
if mibBuilder.loadTexts:fsaTrapCPUrate.setStatus(_A)
_FsaTrapMUrate_Type=DisplayString
_FsaTrapMUrate_Object=MibScalar
fsaTrapMUrate=_FsaTrapMUrate_Object((1,3,6,1,4,1,12356,118,6,3),_FsaTrapMUrate_Type())
fsaTrapMUrate.setMaxAccess(_H)
if mibBuilder.loadTexts:fsaTrapMUrate.setStatus(_A)
_FsaTrapDUrate_Type=DisplayString
_FsaTrapDUrate_Object=MibScalar
fsaTrapDUrate=_FsaTrapDUrate_Object((1,3,6,1,4,1,12356,118,6,4),_FsaTrapDUrate_Type())
fsaTrapDUrate.setMaxAccess(_H)
if mibBuilder.loadTexts:fsaTrapDUrate.setStatus(_A)
_FsaTrapPSUFailure_Type=DisplayString
_FsaTrapPSUFailure_Object=MibScalar
fsaTrapPSUFailure=_FsaTrapPSUFailure_Object((1,3,6,1,4,1,12356,118,6,5),_FsaTrapPSUFailure_Type())
fsaTrapPSUFailure.setMaxAccess(_H)
if mibBuilder.loadTexts:fsaTrapPSUFailure.setStatus(_A)
_FsaTrapHCTopology_Type=DisplayString
_FsaTrapHCTopology_Object=MibScalar
fsaTrapHCTopology=_FsaTrapHCTopology_Object((1,3,6,1,4,1,12356,118,6,6),_FsaTrapHCTopology_Type())
fsaTrapHCTopology.setMaxAccess(_H)
if mibBuilder.loadTexts:fsaTrapHCTopology.setStatus(_A)
_FsaTrapHCHealth_Type=DisplayString
_FsaTrapHCHealth_Object=MibScalar
fsaTrapHCHealth=_FsaTrapHCHealth_Object((1,3,6,1,4,1,12356,118,6,7),_FsaTrapHCHealth_Type())
fsaTrapHCHealth.setMaxAccess(_H)
if mibBuilder.loadTexts:fsaTrapHCHealth.setStatus(_A)
_FsaTrapRaidMsg_Type=DisplayString
_FsaTrapRaidMsg_Object=MibScalar
fsaTrapRaidMsg=_FsaTrapRaidMsg_Object((1,3,6,1,4,1,12356,118,6,8),_FsaTrapRaidMsg_Type())
fsaTrapRaidMsg.setMaxAccess(_H)
if mibBuilder.loadTexts:fsaTrapRaidMsg.setStatus(_A)
_FsaTrapAvgScanTime_Type=DisplayString
_FsaTrapAvgScanTime_Object=MibScalar
fsaTrapAvgScanTime=_FsaTrapAvgScanTime_Object((1,3,6,1,4,1,12356,118,6,9),_FsaTrapAvgScanTime_Type())
fsaTrapAvgScanTime.setMaxAccess(_H)
if mibBuilder.loadTexts:fsaTrapAvgScanTime.setStatus(_A)
_FsaTrapLinkUp_Type=DisplayString
_FsaTrapLinkUp_Object=MibScalar
fsaTrapLinkUp=_FsaTrapLinkUp_Object((1,3,6,1,4,1,12356,118,6,10),_FsaTrapLinkUp_Type())
fsaTrapLinkUp.setMaxAccess(_H)
if mibBuilder.loadTexts:fsaTrapLinkUp.setStatus(_A)
_FsaTrapLinkDown_Type=DisplayString
_FsaTrapLinkDown_Object=MibScalar
fsaTrapLinkDown=_FsaTrapLinkDown_Object((1,3,6,1,4,1,12356,118,6,11),_FsaTrapLinkDown_Type())
fsaTrapLinkDown.setMaxAccess(_H)
if mibBuilder.loadTexts:fsaTrapLinkDown.setStatus(_A)
_FsaTrapContractExpire_Type=DisplayString
_FsaTrapContractExpire_Object=MibScalar
fsaTrapContractExpire=_FsaTrapContractExpire_Object((1,3,6,1,4,1,12356,118,6,12),_FsaTrapContractExpire_Type())
fsaTrapContractExpire.setMaxAccess(_H)
if mibBuilder.loadTexts:fsaTrapContractExpire.setStatus(_A)
_FsaMibConformance_ObjectIdentity=ObjectIdentity
fsaMibConformance=_FsaMibConformance_ObjectIdentity((1,3,6,1,4,1,12356,118,10))
fsaSystemObjectGroup=ObjectGroup((1,3,6,1,4,1,12356,118,10,1))
fsaSystemObjectGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:fsaSystemObjectGroup.setStatus(_A)
fsaSoftwareObjectGroup=ObjectGroup((1,3,6,1,4,1,12356,118,10,2))
fsaSoftwareObjectGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:fsaSoftwareObjectGroup.setStatus(_A)
fsaUserObjectGroup=ObjectGroup((1,3,6,1,4,1,12356,118,10,3))
fsaUserObjectGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:fsaUserObjectGroup.setStatus(_A)
fsaJobObjectGroup=ObjectGroup((1,3,6,1,4,1,12356,118,10,4))
fsaJobObjectGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:fsaJobObjectGroup.setStatus(_A)
fsaTrapMalware=NotificationType((1,3,6,1,4,1,12356,118,2,0,501))
fsaTrapMalware.setObjects(*((_D,_E),(_F,_G),(_B,_p)))
if mibBuilder.loadTexts:fsaTrapMalware.setStatus(_A)
fsaTrapCPUHigh=NotificationType((1,3,6,1,4,1,12356,118,2,0,502))
fsaTrapCPUHigh.setObjects(*((_D,_E),(_F,_G),(_B,_q)))
if mibBuilder.loadTexts:fsaTrapCPUHigh.setStatus(_A)
fsaTrapMemHigh=NotificationType((1,3,6,1,4,1,12356,118,2,0,503))
fsaTrapMemHigh.setObjects(*((_D,_E),(_F,_G),(_B,_r)))
if mibBuilder.loadTexts:fsaTrapMemHigh.setStatus(_A)
fsaTrapDUHigh=NotificationType((1,3,6,1,4,1,12356,118,2,0,504))
fsaTrapDUHigh.setObjects(*((_D,_E),(_F,_G),(_B,_s)))
if mibBuilder.loadTexts:fsaTrapDUHigh.setStatus(_A)
fsaTrapPSUC=NotificationType((1,3,6,1,4,1,12356,118,2,0,505))
fsaTrapPSUC.setObjects(*((_D,_E),(_F,_G),(_B,_t)))
if mibBuilder.loadTexts:fsaTrapPSUC.setStatus(_A)
fsaTrapHCT=NotificationType((1,3,6,1,4,1,12356,118,2,0,506))
fsaTrapHCT.setObjects(*((_D,_E),(_F,_G),(_B,_u)))
if mibBuilder.loadTexts:fsaTrapHCT.setStatus(_A)
fsaTrapHCH=NotificationType((1,3,6,1,4,1,12356,118,2,0,507))
fsaTrapHCH.setObjects(*((_D,_E),(_F,_G),(_B,_v)))
if mibBuilder.loadTexts:fsaTrapHCH.setStatus(_A)
fsaTrapRDM=NotificationType((1,3,6,1,4,1,12356,118,2,0,508))
fsaTrapRDM.setObjects(*((_D,_E),(_F,_G),(_B,_w)))
if mibBuilder.loadTexts:fsaTrapRDM.setStatus(_A)
fsaTrapAST=NotificationType((1,3,6,1,4,1,12356,118,2,0,509))
fsaTrapAST.setObjects(*((_D,_E),(_F,_G),(_B,_x)))
if mibBuilder.loadTexts:fsaTrapAST.setStatus(_A)
fsaTrapLKUP=NotificationType((1,3,6,1,4,1,12356,118,2,0,510))
fsaTrapLKUP.setObjects(*((_D,_E),(_F,_G),(_B,_y)))
if mibBuilder.loadTexts:fsaTrapLKUP.setStatus(_A)
fsaTrapLKDN=NotificationType((1,3,6,1,4,1,12356,118,2,0,511))
fsaTrapLKDN.setObjects(*((_D,_E),(_F,_G),(_B,_z)))
if mibBuilder.loadTexts:fsaTrapLKDN.setStatus(_A)
fsaTrapCntExp=NotificationType((1,3,6,1,4,1,12356,118,2,0,512))
fsaTrapCntExp.setObjects(*((_D,_E),(_F,_G),(_B,_A0)))
if mibBuilder.loadTexts:fsaTrapCntExp.setStatus(_A)
fsaNotificationGroup=NotificationGroup((1,3,6,1,4,1,12356,118,10,5))
fsaNotificationGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:fsaNotificationGroup.setStatus(_A)
fsaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12356,118,10,100))
fsaMIBCompliance.setObjects(*((_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:fsaMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'FsaAdminPermLevel':FsaAdminPermLevel,'FsaUserAuthType':FsaUserAuthType,'FsaSessProto':FsaSessProto,'fnFortiSandboxMib':fnFortiSandboxMib,'fsaModel':fsaModel,'fsa1000D':fsa1000D,'fsaVM':fsaVM,'fsa3000D':fsa3000D,'fsa3500D':fsa3500D,'fsa3000E':fsa3000E,'fsa2000E':fsa2000E,'fsa1000F':fsa1000F,'fsa500F':fsa500F,'fsa3000F':fsa3000F,'fsa1000FDC':fsa1000FDC,'fsaTraps':fsaTraps,'fsaTrapPrefix':fsaTrapPrefix,_A1:fsaTrapMalware,_A2:fsaTrapCPUHigh,_A3:fsaTrapMemHigh,_A4:fsaTrapDUHigh,_A5:fsaTrapPSUC,_A6:fsaTrapHCT,_A7:fsaTrapHCH,_A8:fsaTrapRDM,_A9:fsaTrapAST,_AA:fsaTrapLKUP,_AB:fsaTrapLKDN,_AC:fsaTrapCntExp,'fsaSystem':fsaSystem,'fsaSystemInfo':fsaSystemInfo,_L:fsaSysVersion,_M:fsaSysCpuUsage,_N:fsaSysMemUsage,_O:fsaSysMemCapacity,_P:fsaSysDiskUsage,_Q:fsaSysDiskCapacity,_R:fsaSysCpuUsageExcludedNice,_S:fsaSysUpTime,'fsaSoftware':fsaSoftware,_T:fsaSysTracer,_U:fsaSysRating,_V:fsaSysTool,_W:fsaSysSniffer,_X:fsaSysIPS,'fsaFwUsers':fsaFwUsers,'fsaFwUserInfo':fsaFwUserInfo,_Y:fsaFwUserNumber,_Z:fsaFwUserAuthTimeout,'fsaFwUserTables':fsaFwUserTables,'fsaFwUserTable':fsaFwUserTable,'fsaFwUserEntry':fsaFwUserEntry,_K:fsaFwUserIndex,_a:fsaFwUserName,_b:fsaFwUserAuth,_c:fsaFwUserState,'fsaJobInfo':fsaJobInfo,'fsaJobQueue':fsaJobQueue,_d:fsaFTypeExe,_e:fsaFTypePDF,_f:fsaFTypeDOC,_g:fsaFTypeFLASH,_h:fsaFTypeWEB,_i:fsaFTypeAndroid,_j:fsaFTypeMAC,_k:fsaFTypeURL,_l:fsaFTypeExtra,_m:fsaFTypeNOVM,_n:fsaFTypePre,_o:fsaJobProcessing,'fsaTrapObjects':fsaTrapObjects,_p:fsaTrapJobInfo,_q:fsaTrapCPUrate,_r:fsaTrapMUrate,_s:fsaTrapDUrate,_t:fsaTrapPSUFailure,_u:fsaTrapHCTopology,_v:fsaTrapHCHealth,_w:fsaTrapRaidMsg,_x:fsaTrapAvgScanTime,_y:fsaTrapLinkUp,_z:fsaTrapLinkDown,_A0:fsaTrapContractExpire,'fsaMibConformance':fsaMibConformance,_AE:fsaSystemObjectGroup,_AF:fsaSoftwareObjectGroup,'fsaUserObjectGroup':fsaUserObjectGroup,_AG:fsaJobObjectGroup,_AD:fsaNotificationGroup,'fsaMIBCompliance':fsaMIBCompliance})