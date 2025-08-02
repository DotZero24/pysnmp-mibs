_AC='systemGroup'
_AB='sysMgmtCfgUlResult'
_AA='sysMgmtCfgUlPath'
_A9='sysMgmtCfgDlResult'
_A8='sysMgmtCfgDlPath'
_A7='sysMgmtLicUlResult'
_A6='sysMgmtLicUlPath'
_A5='sysMgmtLicDlResult'
_A4='sysMgmtLicDlPath'
_A3='sysMgmtFrmwUlResult'
_A2='sysMgmtFrmwUlPath'
_A1='sysMgmtFrmwDlResult'
_A0='sysMgmtFrmwDlPath'
_z='sysMgmtHoldTimer'
_y='sysMgmtErrorString'
_x='sysMgmtOperProgress'
_w='sysMgmtCurrentState'
_v='sysMgmtSrcIp'
_u='sysMgmtAccess'
_t='sysQueueDrops'
_s='sysQueueMaxLen'
_r='sysQueueLen'
_q='sysQueueName'
_p='sysNetPagesInUse'
_o='sysNetPagesTotal'
_n='sysNetBufsInUse'
_m='sysMemTotal'
_l='sysMemFree'
_k='sysIfCurLoadTx'
_j='sysIfCurLoadRx'
_i='sysIfCurPpsTx'
_h='sysIfCurPpsRx'
_g='sysBuildTime'
_f='sysBuildDate'
_e='sysFirmwareID'
_d='sysModel'
_c='sysSoftwareVersion'
_b='sysLastRebootReason'
_a='sysNote'
_Z='sysSerialNumberStr'
_Y='sysRestartTimer'
_X='sysSerialNumber'
_W='sysTrapSequence'
_V='sysTemperature'
_U='sysCpu'
_T='sysDropRedirects'
_S='sysSendRedirects'
_R='sysICMPLimit'
_Q='sysFastRoute'
_P='sysGPSXY'
_O='sysIfEntry'
_N='DisplayString'
_M='Unsigned32'
_L='Gauge32'
_K='sysQueueIndex'
_J='off'
_I='blocked'
_H='ftp-error'
_G='system-error'
_F='success'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='AQUASYSTEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifEntry,=mibBuilder.importSymbols('IF-MIB','ifEntry')
wanflex,=mibBuilder.importSymbols('INFINET-MIB','wanflex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_L,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention')
aquasystemMIB=ModuleIdentity((1,3,6,1,4,1,3942,1,1,3))
if mibBuilder.loadTexts:aquasystemMIB.setRevisions(('2018-02-26 10:30','2014-07-29 06:57','2014-06-03 03:50','2014-01-21 07:21','2014-01-15 04:38','2013-07-22 11:04','2013-06-19 16:22','2012-06-13 08:16','2011-02-16 09:34','2008-05-05 09:00','2007-11-08 11:16','2007-08-23 17:32'))
_SysGPSXY_Type=OctetString
_SysGPSXY_Object=MibScalar
sysGPSXY=_SysGPSXY_Object((1,3,6,1,4,1,3942,1,1,3,1),_SysGPSXY_Type())
sysGPSXY.setMaxAccess(_E)
if mibBuilder.loadTexts:sysGPSXY.setStatus(_A)
class _SysFastRoute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_J,2)))
_SysFastRoute_Type.__name__=_D
_SysFastRoute_Object=MibScalar
sysFastRoute=_SysFastRoute_Object((1,3,6,1,4,1,3942,1,1,3,2),_SysFastRoute_Type())
sysFastRoute.setMaxAccess(_E)
if mibBuilder.loadTexts:sysFastRoute.setStatus(_A)
class _SysICMPLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SysICMPLimit_Type.__name__=_D
_SysICMPLimit_Object=MibScalar
sysICMPLimit=_SysICMPLimit_Object((1,3,6,1,4,1,3942,1,1,3,3),_SysICMPLimit_Type())
sysICMPLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:sysICMPLimit.setStatus(_A)
class _SysSendRedirects_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_J,2)))
_SysSendRedirects_Type.__name__=_D
_SysSendRedirects_Object=MibScalar
sysSendRedirects=_SysSendRedirects_Object((1,3,6,1,4,1,3942,1,1,3,4),_SysSendRedirects_Type())
sysSendRedirects.setMaxAccess(_E)
if mibBuilder.loadTexts:sysSendRedirects.setStatus(_A)
class _SysDropRedirects_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_J,2)))
_SysDropRedirects_Type.__name__=_D
_SysDropRedirects_Object=MibScalar
sysDropRedirects=_SysDropRedirects_Object((1,3,6,1,4,1,3942,1,1,3,5),_SysDropRedirects_Type())
sysDropRedirects.setMaxAccess(_E)
if mibBuilder.loadTexts:sysDropRedirects.setStatus(_A)
_SysCpu_Type=Gauge32
_SysCpu_Object=MibScalar
sysCpu=_SysCpu_Object((1,3,6,1,4,1,3942,1,1,3,6),_SysCpu_Type())
sysCpu.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCpu.setStatus(_A)
_SysTemperature_Type=Integer32
_SysTemperature_Object=MibScalar
sysTemperature=_SysTemperature_Object((1,3,6,1,4,1,3942,1,1,3,7),_SysTemperature_Type())
sysTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:sysTemperature.setStatus(_A)
_SysTrapSequence_Type=Counter32
_SysTrapSequence_Object=MibScalar
sysTrapSequence=_SysTrapSequence_Object((1,3,6,1,4,1,3942,1,1,3,8),_SysTrapSequence_Type())
sysTrapSequence.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:sysTrapSequence.setStatus(_A)
_SysSerialNumber_Type=Integer32
_SysSerialNumber_Object=MibScalar
sysSerialNumber=_SysSerialNumber_Object((1,3,6,1,4,1,3942,1,1,3,9),_SysSerialNumber_Type())
sysSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSerialNumber.setStatus(_A)
class _SysRestartTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,107374))
_SysRestartTimer_Type.__name__=_M
_SysRestartTimer_Object=MibScalar
sysRestartTimer=_SysRestartTimer_Object((1,3,6,1,4,1,3942,1,1,3,10),_SysRestartTimer_Type())
sysRestartTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sysRestartTimer.setStatus(_A)
_SysSerialNumberStr_Type=DisplayString
_SysSerialNumberStr_Object=MibScalar
sysSerialNumberStr=_SysSerialNumberStr_Object((1,3,6,1,4,1,3942,1,1,3,11),_SysSerialNumberStr_Type())
sysSerialNumberStr.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSerialNumberStr.setStatus(_A)
_SysNote_Type=OctetString
_SysNote_Object=MibScalar
sysNote=_SysNote_Object((1,3,6,1,4,1,3942,1,1,3,12),_SysNote_Type())
sysNote.setMaxAccess(_E)
if mibBuilder.loadTexts:sysNote.setStatus(_A)
_SysLastRebootReason_Type=DisplayString
_SysLastRebootReason_Object=MibScalar
sysLastRebootReason=_SysLastRebootReason_Object((1,3,6,1,4,1,3942,1,1,3,13),_SysLastRebootReason_Type())
sysLastRebootReason.setMaxAccess(_C)
if mibBuilder.loadTexts:sysLastRebootReason.setStatus(_A)
_SysSoftwareVersion_Type=DisplayString
_SysSoftwareVersion_Object=MibScalar
sysSoftwareVersion=_SysSoftwareVersion_Object((1,3,6,1,4,1,3942,1,1,3,14),_SysSoftwareVersion_Type())
sysSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSoftwareVersion.setStatus(_A)
_SysModel_Type=DisplayString
_SysModel_Object=MibScalar
sysModel=_SysModel_Object((1,3,6,1,4,1,3942,1,1,3,15),_SysModel_Type())
sysModel.setMaxAccess(_C)
if mibBuilder.loadTexts:sysModel.setStatus(_A)
_SysFirmwareID_Type=DisplayString
_SysFirmwareID_Object=MibScalar
sysFirmwareID=_SysFirmwareID_Object((1,3,6,1,4,1,3942,1,1,3,16),_SysFirmwareID_Type())
sysFirmwareID.setMaxAccess(_C)
if mibBuilder.loadTexts:sysFirmwareID.setStatus(_A)
_SysBuildDate_Type=DisplayString
_SysBuildDate_Object=MibScalar
sysBuildDate=_SysBuildDate_Object((1,3,6,1,4,1,3942,1,1,3,17),_SysBuildDate_Type())
sysBuildDate.setMaxAccess(_C)
if mibBuilder.loadTexts:sysBuildDate.setStatus(_A)
_SysBuildTime_Type=DisplayString
_SysBuildTime_Object=MibScalar
sysBuildTime=_SysBuildTime_Object((1,3,6,1,4,1,3942,1,1,3,18),_SysBuildTime_Type())
sysBuildTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sysBuildTime.setStatus(_A)
_SysIf_ObjectIdentity=ObjectIdentity
sysIf=_SysIf_ObjectIdentity((1,3,6,1,4,1,3942,1,1,3,20))
_SysIfTable_Object=MibTable
sysIfTable=_SysIfTable_Object((1,3,6,1,4,1,3942,1,1,3,20,1))
if mibBuilder.loadTexts:sysIfTable.setStatus(_A)
_SysIfEntry_Object=MibTableRow
sysIfEntry=_SysIfEntry_Object((1,3,6,1,4,1,3942,1,1,3,20,1,1))
if mibBuilder.loadTexts:sysIfEntry.setStatus(_A)
_SysIfCurPpsRx_Type=Gauge32
_SysIfCurPpsRx_Object=MibTableColumn
sysIfCurPpsRx=_SysIfCurPpsRx_Object((1,3,6,1,4,1,3942,1,1,3,20,1,1,1),_SysIfCurPpsRx_Type())
sysIfCurPpsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysIfCurPpsRx.setStatus(_A)
_SysIfCurPpsTx_Type=Gauge32
_SysIfCurPpsTx_Object=MibTableColumn
sysIfCurPpsTx=_SysIfCurPpsTx_Object((1,3,6,1,4,1,3942,1,1,3,20,1,1,2),_SysIfCurPpsTx_Type())
sysIfCurPpsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysIfCurPpsTx.setStatus(_A)
_SysIfCurLoadRx_Type=Gauge32
_SysIfCurLoadRx_Object=MibTableColumn
sysIfCurLoadRx=_SysIfCurLoadRx_Object((1,3,6,1,4,1,3942,1,1,3,20,1,1,3),_SysIfCurLoadRx_Type())
sysIfCurLoadRx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysIfCurLoadRx.setStatus(_A)
_SysIfCurLoadTx_Type=Gauge32
_SysIfCurLoadTx_Object=MibTableColumn
sysIfCurLoadTx=_SysIfCurLoadTx_Object((1,3,6,1,4,1,3942,1,1,3,20,1,1,4),_SysIfCurLoadTx_Type())
sysIfCurLoadTx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysIfCurLoadTx.setStatus(_A)
_SysMem_ObjectIdentity=ObjectIdentity
sysMem=_SysMem_ObjectIdentity((1,3,6,1,4,1,3942,1,1,3,21))
_SysMemTotal_Type=Gauge32
_SysMemTotal_Object=MibScalar
sysMemTotal=_SysMemTotal_Object((1,3,6,1,4,1,3942,1,1,3,21,1),_SysMemTotal_Type())
sysMemTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMemTotal.setStatus(_A)
_SysMemFree_Type=Gauge32
_SysMemFree_Object=MibScalar
sysMemFree=_SysMemFree_Object((1,3,6,1,4,1,3942,1,1,3,21,2),_SysMemFree_Type())
sysMemFree.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMemFree.setStatus(_A)
_SysNetBufsInUse_Type=Gauge32
_SysNetBufsInUse_Object=MibScalar
sysNetBufsInUse=_SysNetBufsInUse_Object((1,3,6,1,4,1,3942,1,1,3,21,3),_SysNetBufsInUse_Type())
sysNetBufsInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:sysNetBufsInUse.setStatus(_A)
_SysNetPagesTotal_Type=Gauge32
_SysNetPagesTotal_Object=MibScalar
sysNetPagesTotal=_SysNetPagesTotal_Object((1,3,6,1,4,1,3942,1,1,3,21,4),_SysNetPagesTotal_Type())
sysNetPagesTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:sysNetPagesTotal.setStatus(_A)
_SysNetPagesInUse_Type=Gauge32
_SysNetPagesInUse_Object=MibScalar
sysNetPagesInUse=_SysNetPagesInUse_Object((1,3,6,1,4,1,3942,1,1,3,21,5),_SysNetPagesInUse_Type())
sysNetPagesInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:sysNetPagesInUse.setStatus(_A)
_SysQueue_ObjectIdentity=ObjectIdentity
sysQueue=_SysQueue_ObjectIdentity((1,3,6,1,4,1,3942,1,1,3,22))
_SysQueueTable_Object=MibTable
sysQueueTable=_SysQueueTable_Object((1,3,6,1,4,1,3942,1,1,3,22,1))
if mibBuilder.loadTexts:sysQueueTable.setStatus(_A)
_SysQueueEntry_Object=MibTableRow
sysQueueEntry=_SysQueueEntry_Object((1,3,6,1,4,1,3942,1,1,3,22,1,1))
sysQueueEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:sysQueueEntry.setStatus(_A)
class _SysQueueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SysQueueIndex_Type.__name__=_D
_SysQueueIndex_Object=MibTableColumn
sysQueueIndex=_SysQueueIndex_Object((1,3,6,1,4,1,3942,1,1,3,22,1,1,1),_SysQueueIndex_Type())
sysQueueIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sysQueueIndex.setStatus(_A)
_SysQueueName_Type=OctetString
_SysQueueName_Object=MibTableColumn
sysQueueName=_SysQueueName_Object((1,3,6,1,4,1,3942,1,1,3,22,1,1,2),_SysQueueName_Type())
sysQueueName.setMaxAccess(_C)
if mibBuilder.loadTexts:sysQueueName.setStatus(_A)
_SysQueueLen_Type=Unsigned32
_SysQueueLen_Object=MibTableColumn
sysQueueLen=_SysQueueLen_Object((1,3,6,1,4,1,3942,1,1,3,22,1,1,3),_SysQueueLen_Type())
sysQueueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:sysQueueLen.setStatus(_A)
_SysQueueMaxLen_Type=Unsigned32
_SysQueueMaxLen_Object=MibTableColumn
sysQueueMaxLen=_SysQueueMaxLen_Object((1,3,6,1,4,1,3942,1,1,3,22,1,1,4),_SysQueueMaxLen_Type())
sysQueueMaxLen.setMaxAccess(_C)
if mibBuilder.loadTexts:sysQueueMaxLen.setStatus(_A)
_SysQueueDrops_Type=Unsigned32
_SysQueueDrops_Object=MibTableColumn
sysQueueDrops=_SysQueueDrops_Object((1,3,6,1,4,1,3942,1,1,3,22,1,1,5),_SysQueueDrops_Type())
sysQueueDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:sysQueueDrops.setStatus(_A)
_SysMgmt_ObjectIdentity=ObjectIdentity
sysMgmt=_SysMgmt_ObjectIdentity((1,3,6,1,4,1,3942,1,1,3,23))
_SysMgmtGlobals_ObjectIdentity=ObjectIdentity
sysMgmtGlobals=_SysMgmtGlobals_ObjectIdentity((1,3,6,1,4,1,3942,1,1,3,23,1))
_SysMgmtAccess_Type=DisplayString
_SysMgmtAccess_Object=MibScalar
sysMgmtAccess=_SysMgmtAccess_Object((1,3,6,1,4,1,3942,1,1,3,23,1,1),_SysMgmtAccess_Type())
sysMgmtAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMgmtAccess.setStatus(_A)
_SysMgmtSrcIp_Type=IpAddress
_SysMgmtSrcIp_Object=MibScalar
sysMgmtSrcIp=_SysMgmtSrcIp_Object((1,3,6,1,4,1,3942,1,1,3,23,1,2),_SysMgmtSrcIp_Type())
sysMgmtSrcIp.setMaxAccess(_E)
if mibBuilder.loadTexts:sysMgmtSrcIp.setStatus(_A)
class _SysMgmtCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('idle',0),('busy',1),('hold',2)))
_SysMgmtCurrentState_Type.__name__=_D
_SysMgmtCurrentState_Object=MibScalar
sysMgmtCurrentState=_SysMgmtCurrentState_Object((1,3,6,1,4,1,3942,1,1,3,23,1,3),_SysMgmtCurrentState_Type())
sysMgmtCurrentState.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMgmtCurrentState.setStatus(_A)
class _SysMgmtOperProgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SysMgmtOperProgress_Type.__name__=_D
_SysMgmtOperProgress_Object=MibScalar
sysMgmtOperProgress=_SysMgmtOperProgress_Object((1,3,6,1,4,1,3942,1,1,3,23,1,4),_SysMgmtOperProgress_Type())
sysMgmtOperProgress.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMgmtOperProgress.setStatus(_A)
_SysMgmtErrorString_Type=DisplayString
_SysMgmtErrorString_Object=MibScalar
sysMgmtErrorString=_SysMgmtErrorString_Object((1,3,6,1,4,1,3942,1,1,3,23,1,5),_SysMgmtErrorString_Type())
sysMgmtErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMgmtErrorString.setStatus(_A)
class _SysMgmtHoldTimer_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_SysMgmtHoldTimer_Type.__name__=_L
_SysMgmtHoldTimer_Object=MibScalar
sysMgmtHoldTimer=_SysMgmtHoldTimer_Object((1,3,6,1,4,1,3942,1,1,3,23,1,6),_SysMgmtHoldTimer_Type())
sysMgmtHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMgmtHoldTimer.setStatus(_A)
_SysMgmtFrmw_ObjectIdentity=ObjectIdentity
sysMgmtFrmw=_SysMgmtFrmw_ObjectIdentity((1,3,6,1,4,1,3942,1,1,3,23,2))
class _SysMgmtFrmwDlPath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_SysMgmtFrmwDlPath_Type.__name__=_N
_SysMgmtFrmwDlPath_Object=MibScalar
sysMgmtFrmwDlPath=_SysMgmtFrmwDlPath_Object((1,3,6,1,4,1,3942,1,1,3,23,2,1),_SysMgmtFrmwDlPath_Type())
sysMgmtFrmwDlPath.setMaxAccess(_E)
if mibBuilder.loadTexts:sysMgmtFrmwDlPath.setStatus(_A)
class _SysMgmtFrmwDlResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),('firmware-error',3),(_I,4)))
_SysMgmtFrmwDlResult_Type.__name__=_D
_SysMgmtFrmwDlResult_Object=MibScalar
sysMgmtFrmwDlResult=_SysMgmtFrmwDlResult_Object((1,3,6,1,4,1,3942,1,1,3,23,2,2),_SysMgmtFrmwDlResult_Type())
sysMgmtFrmwDlResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMgmtFrmwDlResult.setStatus(_A)
_SysMgmtFrmwUlPath_Type=DisplayString
_SysMgmtFrmwUlPath_Object=MibScalar
sysMgmtFrmwUlPath=_SysMgmtFrmwUlPath_Object((1,3,6,1,4,1,3942,1,1,3,23,2,3),_SysMgmtFrmwUlPath_Type())
sysMgmtFrmwUlPath.setMaxAccess(_E)
if mibBuilder.loadTexts:sysMgmtFrmwUlPath.setStatus(_A)
class _SysMgmtFrmwUlResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3)))
_SysMgmtFrmwUlResult_Type.__name__=_D
_SysMgmtFrmwUlResult_Object=MibScalar
sysMgmtFrmwUlResult=_SysMgmtFrmwUlResult_Object((1,3,6,1,4,1,3942,1,1,3,23,2,4),_SysMgmtFrmwUlResult_Type())
sysMgmtFrmwUlResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMgmtFrmwUlResult.setStatus(_A)
_SysMgmtLic_ObjectIdentity=ObjectIdentity
sysMgmtLic=_SysMgmtLic_ObjectIdentity((1,3,6,1,4,1,3942,1,1,3,23,3))
_SysMgmtLicDlPath_Type=DisplayString
_SysMgmtLicDlPath_Object=MibScalar
sysMgmtLicDlPath=_SysMgmtLicDlPath_Object((1,3,6,1,4,1,3942,1,1,3,23,3,1),_SysMgmtLicDlPath_Type())
sysMgmtLicDlPath.setMaxAccess(_E)
if mibBuilder.loadTexts:sysMgmtLicDlPath.setStatus(_A)
class _SysMgmtLicDlResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),('license-error',3),(_I,4)))
_SysMgmtLicDlResult_Type.__name__=_D
_SysMgmtLicDlResult_Object=MibScalar
sysMgmtLicDlResult=_SysMgmtLicDlResult_Object((1,3,6,1,4,1,3942,1,1,3,23,3,2),_SysMgmtLicDlResult_Type())
sysMgmtLicDlResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMgmtLicDlResult.setStatus(_A)
_SysMgmtLicUlPath_Type=DisplayString
_SysMgmtLicUlPath_Object=MibScalar
sysMgmtLicUlPath=_SysMgmtLicUlPath_Object((1,3,6,1,4,1,3942,1,1,3,23,3,3),_SysMgmtLicUlPath_Type())
sysMgmtLicUlPath.setMaxAccess(_E)
if mibBuilder.loadTexts:sysMgmtLicUlPath.setStatus(_A)
class _SysMgmtLicUlResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3)))
_SysMgmtLicUlResult_Type.__name__=_D
_SysMgmtLicUlResult_Object=MibScalar
sysMgmtLicUlResult=_SysMgmtLicUlResult_Object((1,3,6,1,4,1,3942,1,1,3,23,3,4),_SysMgmtLicUlResult_Type())
sysMgmtLicUlResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMgmtLicUlResult.setStatus(_A)
_SysMgmtCfg_ObjectIdentity=ObjectIdentity
sysMgmtCfg=_SysMgmtCfg_ObjectIdentity((1,3,6,1,4,1,3942,1,1,3,23,4))
_SysMgmtCfgDlPath_Type=DisplayString
_SysMgmtCfgDlPath_Object=MibScalar
sysMgmtCfgDlPath=_SysMgmtCfgDlPath_Object((1,3,6,1,4,1,3942,1,1,3,23,4,1),_SysMgmtCfgDlPath_Type())
sysMgmtCfgDlPath.setMaxAccess(_E)
if mibBuilder.loadTexts:sysMgmtCfgDlPath.setStatus(_A)
class _SysMgmtCfgDlResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),('config-error',3),(_I,4)))
_SysMgmtCfgDlResult_Type.__name__=_D
_SysMgmtCfgDlResult_Object=MibScalar
sysMgmtCfgDlResult=_SysMgmtCfgDlResult_Object((1,3,6,1,4,1,3942,1,1,3,23,4,2),_SysMgmtCfgDlResult_Type())
sysMgmtCfgDlResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMgmtCfgDlResult.setStatus(_A)
_SysMgmtCfgUlPath_Type=DisplayString
_SysMgmtCfgUlPath_Object=MibScalar
sysMgmtCfgUlPath=_SysMgmtCfgUlPath_Object((1,3,6,1,4,1,3942,1,1,3,23,4,3),_SysMgmtCfgUlPath_Type())
sysMgmtCfgUlPath.setMaxAccess(_E)
if mibBuilder.loadTexts:sysMgmtCfgUlPath.setStatus(_A)
class _SysMgmtCfgUlResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3)))
_SysMgmtCfgUlResult_Type.__name__=_D
_SysMgmtCfgUlResult_Object=MibScalar
sysMgmtCfgUlResult=_SysMgmtCfgUlResult_Object((1,3,6,1,4,1,3942,1,1,3,23,4,4),_SysMgmtCfgUlResult_Type())
sysMgmtCfgUlResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sysMgmtCfgUlResult.setStatus(_A)
_AquasystemMIBConformance_ObjectIdentity=ObjectIdentity
aquasystemMIBConformance=_AquasystemMIBConformance_ObjectIdentity((1,3,6,1,4,1,3942,1,1,3,100))
_AquasystemMIBCompliances_ObjectIdentity=ObjectIdentity
aquasystemMIBCompliances=_AquasystemMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3942,1,1,3,100,1))
_AquasystemMIBGroups_ObjectIdentity=ObjectIdentity
aquasystemMIBGroups=_AquasystemMIBGroups_ObjectIdentity((1,3,6,1,4,1,3942,1,1,3,100,2))
ifEntry.registerAugmentions((_B,_O))
sysIfEntry.setIndexNames(*ifEntry.getIndexNames())
systemGroup=ObjectGroup((1,3,6,1,4,1,3942,1,1,3,100,2,1))
systemGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_K),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:systemGroup.setStatus(_A)
aquasystemMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3942,1,1,3,100,1,1))
aquasystemMIBCompliance.setObjects((_B,_AC))
if mibBuilder.loadTexts:aquasystemMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aquasystemMIB':aquasystemMIB,_P:sysGPSXY,_Q:sysFastRoute,_R:sysICMPLimit,_S:sysSendRedirects,_T:sysDropRedirects,_U:sysCpu,_V:sysTemperature,_W:sysTrapSequence,_X:sysSerialNumber,_Y:sysRestartTimer,_Z:sysSerialNumberStr,_a:sysNote,_b:sysLastRebootReason,_c:sysSoftwareVersion,_d:sysModel,_e:sysFirmwareID,_f:sysBuildDate,_g:sysBuildTime,'sysIf':sysIf,'sysIfTable':sysIfTable,_O:sysIfEntry,_h:sysIfCurPpsRx,_i:sysIfCurPpsTx,_j:sysIfCurLoadRx,_k:sysIfCurLoadTx,'sysMem':sysMem,_m:sysMemTotal,_l:sysMemFree,_n:sysNetBufsInUse,_o:sysNetPagesTotal,_p:sysNetPagesInUse,'sysQueue':sysQueue,'sysQueueTable':sysQueueTable,'sysQueueEntry':sysQueueEntry,_K:sysQueueIndex,_q:sysQueueName,_r:sysQueueLen,_s:sysQueueMaxLen,_t:sysQueueDrops,'sysMgmt':sysMgmt,'sysMgmtGlobals':sysMgmtGlobals,_u:sysMgmtAccess,_v:sysMgmtSrcIp,_w:sysMgmtCurrentState,_x:sysMgmtOperProgress,_y:sysMgmtErrorString,_z:sysMgmtHoldTimer,'sysMgmtFrmw':sysMgmtFrmw,_A0:sysMgmtFrmwDlPath,_A1:sysMgmtFrmwDlResult,_A2:sysMgmtFrmwUlPath,_A3:sysMgmtFrmwUlResult,'sysMgmtLic':sysMgmtLic,_A4:sysMgmtLicDlPath,_A5:sysMgmtLicDlResult,_A6:sysMgmtLicUlPath,_A7:sysMgmtLicUlResult,'sysMgmtCfg':sysMgmtCfg,_A8:sysMgmtCfgDlPath,_A9:sysMgmtCfgDlResult,_AA:sysMgmtCfgUlPath,_AB:sysMgmtCfgUlResult,'aquasystemMIBConformance':aquasystemMIBConformance,'aquasystemMIBCompliances':aquasystemMIBCompliances,'aquasystemMIBCompliance':aquasystemMIBCompliance,'aquasystemMIBGroups':aquasystemMIBGroups,_AC:systemGroup})