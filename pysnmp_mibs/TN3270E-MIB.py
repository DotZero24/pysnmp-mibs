_Ap='tn3270eHiCapacityGroup'
_Ao='tn3270eResMapGroup'
_An='tn3270eSessionGroup'
_Am='tn3270eBasicGroup'
_Al='tn3270eSrvrStatsHCOutOctets'
_Ak='tn3270eSrvrStatsHCInOctets'
_Aj='tn3270eTcpConnStateLastDiscReason'
_Ai='tn3270eTcpConnSnaState'
_Ah='tn3270eTcpConnLuLuBindImage'
_Ag='tn3270eTcpConnLogInfo'
_Af='tn3270eTcpConnTraceData'
_Ae='tn3270eTcpConnClientId'
_Ad='tn3270eTcpConnClientIdFormat'
_Ac='tn3270eTcpConnId'
_Ab='tn3270eClientResMapRowStatus'
_Aa='tn3270eResPoolRowStatus'
_AZ='tn3270eResPoolElementType'
_AY='tn3270eTcpConnActivationTime'
_AX='tn3270eTcpConnSrvrConfIndex'
_AW='tn3270eTcpConnFunctions'
_AV='tn3270eTcpConnDeviceType'
_AU='tn3270eTcpConnResourceType'
_AT='tn3270eTcpConnResourceElement'
_AS='tn3270eTcpConnBytesOut'
_AR='tn3270eTcpConnBytesIn'
_AQ='tn3270eTcpConnLastActivity'
_AP='tn3270eResMapSscpSuppliedName'
_AO='tn3270eResMapElementType'
_AN='tn3270eResMapPort'
_AM='tn3270eResMapAddress'
_AL='tn3270eResMapAddrType'
_AK='tn3270eConfSpinLock'
_AJ='tn3270eSnaMapPrimaryLuName'
_AI='tn3270eSnaMapLocalName'
_AH='tn3270eClientGroupRowStatus'
_AG='tn3270eClientGroupPfxLength'
_AF='tn3270eClientGroupSubnetMask'
_AE='tn3270eSrvrStatsConnErrorRejs'
_AD='tn3270eSrvrStatsOutOctets'
_AC='tn3270eSrvrStatsInOctets'
_AB='tn3270eSrvrStatsDisconnects'
_AA='tn3270eSrvrStatsConnResrceRejs'
_A9='tn3270eSrvrStatsInConnects'
_A8='tn3270eSrvrStatsSparePtrs'
_A7='tn3270eSrvrStatsInUsePtrs'
_A6='tn3270eSrvrStatsMaxPtrs'
_A5='tn3270eSrvrStatsSpareTerms'
_A4='tn3270eSrvrStatsInUseTerms'
_A3='tn3270eSrvrStatsMaxTerms'
_A2='tn3270eSrvrStatsUpTime'
_A1='tn3270eSrvrPortRowStatus'
_A0='tn3270eSrvrConfTmTimeout'
_z='tn3270eSrvrConfLastActTime'
_y='tn3270eSrvrConfRowStatus'
_x='tn3270eSrvrConfContact'
_w='tn3270eSrvrConfSrvrType'
_v='tn3270eSrvrConfSessionTermState'
_u='tn3270eSrvrConfOperStatus'
_t='tn3270eSrvrConfAdminStatus'
_s='tn3270eSrvrFunctionsSupported'
_r='tn3270eSrvrConfTmNopInterval'
_q='tn3270eSrvrConfTmNopInactTime'
_p='tn3270eSrvrConfConnectivityChk'
_o='tn3270eSrvrConfInactivityTimeout'
_n='unknown'
_m='tn3270eTcpConnLocalPort'
_l='tn3270eTcpConnLocalAddress'
_k='tn3270eTcpConnLocalAddrType'
_j='tn3270eTcpConnRemPort'
_i='tn3270eTcpConnRemAddress'
_h='tn3270eTcpConnRemAddrType'
_g='tn3270eResMapElementName'
_f='tn3270eClientResMapClientPort'
_e='tn3270eClientResMapClientGroupName'
_d='tn3270eClientResMapPoolName'
_c='tn3270eSnaMapSscpSuppliedName'
_b='tn3270eResPoolElementName'
_a='tn3270eResPoolName'
_Z='tn3270eClientGroupAddress'
_Y='tn3270eClientGroupAddrType'
_X='tn3270eClientGroupName'
_W='connection attempts'
_V='Printer Resources'
_U='DateAndTime'
_T='TimeTicks'
_S='IpAddress'
_R='SnmpAdminString'
_Q='IANATn3270Functions'
_P='LUs'
_O='tn3270eSrvrPortAddress'
_N='tn3270eSrvrPortAddrType'
_M='tn3270eSrvrPort'
_L='OctetString'
_K='seconds'
_J='Utf8String'
_I='octets'
_H='Integer32'
_G='tn3270eSrvrConfIndex'
_F='Unsigned32'
_E='read-create'
_D='not-accessible'
_C='read-only'
_B='TN3270E-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANATn3270DeviceType,IANATn3270Functions,IANATn3270ResourceType,IANATn3270eAddrType,IANATn3270eAddress,IANATn3270eClientType,IANATn3270eLogData=mibBuilder.importSymbols('IANATn3270eTC-MIB','IANATn3270DeviceType',_Q,'IANATn3270ResourceType','IANATn3270eAddrType','IANATn3270eAddress','IANATn3270eClientType','IANATn3270eLogData')
snanauMIB,=mibBuilder.importSymbols('SNA-NAU-MIB','snanauMIB')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,_S,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_T,_F,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_U,'DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp')
Utf8String,=mibBuilder.importSymbols('SYSAPPL-MIB',_J)
tn3270eMIB=ModuleIdentity((1,3,6,1,2,1,34,8))
if mibBuilder.loadTexts:tn3270eMIB.setRevisions(('2006-01-13 00:00','1998-07-27 00:00'))
class SnaResourceName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
class Tn3270eTraceData(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(3,4096))
_Tn3270eNotifications_ObjectIdentity=ObjectIdentity
tn3270eNotifications=_Tn3270eNotifications_ObjectIdentity((1,3,6,1,2,1,34,8,0))
_Tn3270eObjects_ObjectIdentity=ObjectIdentity
tn3270eObjects=_Tn3270eObjects_ObjectIdentity((1,3,6,1,2,1,34,8,1))
_Tn3270eSrvrConfTable_Object=MibTable
tn3270eSrvrConfTable=_Tn3270eSrvrConfTable_Object((1,3,6,1,2,1,34,8,1,1))
if mibBuilder.loadTexts:tn3270eSrvrConfTable.setStatus(_A)
_Tn3270eSrvrConfEntry_Object=MibTableRow
tn3270eSrvrConfEntry=_Tn3270eSrvrConfEntry_Object((1,3,6,1,2,1,34,8,1,1,1))
tn3270eSrvrConfEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:tn3270eSrvrConfEntry.setStatus(_A)
class _Tn3270eSrvrConfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Tn3270eSrvrConfIndex_Type.__name__=_F
_Tn3270eSrvrConfIndex_Object=MibTableColumn
tn3270eSrvrConfIndex=_Tn3270eSrvrConfIndex_Object((1,3,6,1,2,1,34,8,1,1,1,1),_Tn3270eSrvrConfIndex_Type())
tn3270eSrvrConfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eSrvrConfIndex.setStatus(_A)
class _Tn3270eSrvrConfInactivityTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999999))
_Tn3270eSrvrConfInactivityTimeout_Type.__name__=_F
_Tn3270eSrvrConfInactivityTimeout_Object=MibTableColumn
tn3270eSrvrConfInactivityTimeout=_Tn3270eSrvrConfInactivityTimeout_Object((1,3,6,1,2,1,34,8,1,1,1,2),_Tn3270eSrvrConfInactivityTimeout_Type())
tn3270eSrvrConfInactivityTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eSrvrConfInactivityTimeout.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrConfInactivityTimeout.setUnits(_K)
class _Tn3270eSrvrConfConnectivityChk_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('timingMark',1),('nop',2),('noCheck',3)))
_Tn3270eSrvrConfConnectivityChk_Type.__name__=_H
_Tn3270eSrvrConfConnectivityChk_Object=MibTableColumn
tn3270eSrvrConfConnectivityChk=_Tn3270eSrvrConfConnectivityChk_Object((1,3,6,1,2,1,34,8,1,1,1,3),_Tn3270eSrvrConfConnectivityChk_Type())
tn3270eSrvrConfConnectivityChk.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eSrvrConfConnectivityChk.setStatus(_A)
class _Tn3270eSrvrConfTmNopInactTime_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_Tn3270eSrvrConfTmNopInactTime_Type.__name__=_F
_Tn3270eSrvrConfTmNopInactTime_Object=MibTableColumn
tn3270eSrvrConfTmNopInactTime=_Tn3270eSrvrConfTmNopInactTime_Object((1,3,6,1,2,1,34,8,1,1,1,4),_Tn3270eSrvrConfTmNopInactTime_Type())
tn3270eSrvrConfTmNopInactTime.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eSrvrConfTmNopInactTime.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrConfTmNopInactTime.setUnits(_K)
class _Tn3270eSrvrConfTmNopInterval_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_Tn3270eSrvrConfTmNopInterval_Type.__name__=_F
_Tn3270eSrvrConfTmNopInterval_Object=MibTableColumn
tn3270eSrvrConfTmNopInterval=_Tn3270eSrvrConfTmNopInterval_Object((1,3,6,1,2,1,34,8,1,1,1,5),_Tn3270eSrvrConfTmNopInterval_Type())
tn3270eSrvrConfTmNopInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eSrvrConfTmNopInterval.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrConfTmNopInterval.setUnits(_K)
class _Tn3270eSrvrFunctionsSupported_Type(IANATn3270Functions):defaultBinValue='0000011111'
_Tn3270eSrvrFunctionsSupported_Type.__name__=_Q
_Tn3270eSrvrFunctionsSupported_Object=MibTableColumn
tn3270eSrvrFunctionsSupported=_Tn3270eSrvrFunctionsSupported_Object((1,3,6,1,2,1,34,8,1,1,1,6),_Tn3270eSrvrFunctionsSupported_Type())
tn3270eSrvrFunctionsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrFunctionsSupported.setStatus(_A)
class _Tn3270eSrvrConfAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('stopImmediate',3)))
_Tn3270eSrvrConfAdminStatus_Type.__name__=_H
_Tn3270eSrvrConfAdminStatus_Object=MibTableColumn
tn3270eSrvrConfAdminStatus=_Tn3270eSrvrConfAdminStatus_Object((1,3,6,1,2,1,34,8,1,1,1,7),_Tn3270eSrvrConfAdminStatus_Type())
tn3270eSrvrConfAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eSrvrConfAdminStatus.setStatus(_A)
class _Tn3270eSrvrConfOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('busy',3),('shuttingDown',4)))
_Tn3270eSrvrConfOperStatus_Type.__name__=_H
_Tn3270eSrvrConfOperStatus_Object=MibTableColumn
tn3270eSrvrConfOperStatus=_Tn3270eSrvrConfOperStatus_Object((1,3,6,1,2,1,34,8,1,1,1,8),_Tn3270eSrvrConfOperStatus_Type())
tn3270eSrvrConfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrConfOperStatus.setStatus(_A)
class _Tn3270eSrvrConfSessionTermState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('terminate',1),('luSessionPend',2),('queueSession',3)))
_Tn3270eSrvrConfSessionTermState_Type.__name__=_H
_Tn3270eSrvrConfSessionTermState_Object=MibTableColumn
tn3270eSrvrConfSessionTermState=_Tn3270eSrvrConfSessionTermState_Object((1,3,6,1,2,1,34,8,1,1,1,9),_Tn3270eSrvrConfSessionTermState_Type())
tn3270eSrvrConfSessionTermState.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eSrvrConfSessionTermState.setStatus(_A)
class _Tn3270eSrvrConfSrvrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('host',1),('gateway',2)))
_Tn3270eSrvrConfSrvrType_Type.__name__=_H
_Tn3270eSrvrConfSrvrType_Object=MibTableColumn
tn3270eSrvrConfSrvrType=_Tn3270eSrvrConfSrvrType_Object((1,3,6,1,2,1,34,8,1,1,1,10),_Tn3270eSrvrConfSrvrType_Type())
tn3270eSrvrConfSrvrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrConfSrvrType.setStatus(_A)
class _Tn3270eSrvrConfContact_Type(SnmpAdminString):defaultHexValue=''
_Tn3270eSrvrConfContact_Type.__name__=_R
_Tn3270eSrvrConfContact_Object=MibTableColumn
tn3270eSrvrConfContact=_Tn3270eSrvrConfContact_Object((1,3,6,1,2,1,34,8,1,1,1,11),_Tn3270eSrvrConfContact_Type())
tn3270eSrvrConfContact.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eSrvrConfContact.setStatus(_A)
_Tn3270eSrvrConfRowStatus_Type=RowStatus
_Tn3270eSrvrConfRowStatus_Object=MibTableColumn
tn3270eSrvrConfRowStatus=_Tn3270eSrvrConfRowStatus_Object((1,3,6,1,2,1,34,8,1,1,1,12),_Tn3270eSrvrConfRowStatus_Type())
tn3270eSrvrConfRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eSrvrConfRowStatus.setStatus(_A)
class _Tn3270eSrvrConfLastActTime_Type(DateAndTime):defaultHexValue='0000000000000000'
_Tn3270eSrvrConfLastActTime_Type.__name__=_U
_Tn3270eSrvrConfLastActTime_Object=MibTableColumn
tn3270eSrvrConfLastActTime=_Tn3270eSrvrConfLastActTime_Object((1,3,6,1,2,1,34,8,1,1,1,13),_Tn3270eSrvrConfLastActTime_Type())
tn3270eSrvrConfLastActTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrConfLastActTime.setStatus(_A)
class _Tn3270eSrvrConfTmTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_Tn3270eSrvrConfTmTimeout_Type.__name__=_F
_Tn3270eSrvrConfTmTimeout_Object=MibTableColumn
tn3270eSrvrConfTmTimeout=_Tn3270eSrvrConfTmTimeout_Object((1,3,6,1,2,1,34,8,1,1,1,14),_Tn3270eSrvrConfTmTimeout_Type())
tn3270eSrvrConfTmTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eSrvrConfTmTimeout.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrConfTmTimeout.setUnits(_K)
_Tn3270eSrvrPortTable_Object=MibTable
tn3270eSrvrPortTable=_Tn3270eSrvrPortTable_Object((1,3,6,1,2,1,34,8,1,2))
if mibBuilder.loadTexts:tn3270eSrvrPortTable.setStatus(_A)
_Tn3270eSrvrPortEntry_Object=MibTableRow
tn3270eSrvrPortEntry=_Tn3270eSrvrPortEntry_Object((1,3,6,1,2,1,34,8,1,2,1))
tn3270eSrvrPortEntry.setIndexNames((0,_B,_G),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:tn3270eSrvrPortEntry.setStatus(_A)
class _Tn3270eSrvrPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tn3270eSrvrPort_Type.__name__=_F
_Tn3270eSrvrPort_Object=MibTableColumn
tn3270eSrvrPort=_Tn3270eSrvrPort_Object((1,3,6,1,2,1,34,8,1,2,1,1),_Tn3270eSrvrPort_Type())
tn3270eSrvrPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eSrvrPort.setStatus(_A)
_Tn3270eSrvrPortAddrType_Type=IANATn3270eAddrType
_Tn3270eSrvrPortAddrType_Object=MibTableColumn
tn3270eSrvrPortAddrType=_Tn3270eSrvrPortAddrType_Object((1,3,6,1,2,1,34,8,1,2,1,2),_Tn3270eSrvrPortAddrType_Type())
tn3270eSrvrPortAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eSrvrPortAddrType.setStatus(_A)
_Tn3270eSrvrPortAddress_Type=IANATn3270eAddress
_Tn3270eSrvrPortAddress_Object=MibTableColumn
tn3270eSrvrPortAddress=_Tn3270eSrvrPortAddress_Object((1,3,6,1,2,1,34,8,1,2,1,3),_Tn3270eSrvrPortAddress_Type())
tn3270eSrvrPortAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eSrvrPortAddress.setStatus(_A)
_Tn3270eSrvrPortRowStatus_Type=RowStatus
_Tn3270eSrvrPortRowStatus_Object=MibTableColumn
tn3270eSrvrPortRowStatus=_Tn3270eSrvrPortRowStatus_Object((1,3,6,1,2,1,34,8,1,2,1,4),_Tn3270eSrvrPortRowStatus_Type())
tn3270eSrvrPortRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eSrvrPortRowStatus.setStatus(_A)
_Tn3270eSrvrStatsTable_Object=MibTable
tn3270eSrvrStatsTable=_Tn3270eSrvrStatsTable_Object((1,3,6,1,2,1,34,8,1,3))
if mibBuilder.loadTexts:tn3270eSrvrStatsTable.setStatus(_A)
_Tn3270eSrvrStatsEntry_Object=MibTableRow
tn3270eSrvrStatsEntry=_Tn3270eSrvrStatsEntry_Object((1,3,6,1,2,1,34,8,1,3,1))
tn3270eSrvrStatsEntry.setIndexNames((0,_B,_G),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:tn3270eSrvrStatsEntry.setStatus(_A)
_Tn3270eSrvrStatsUpTime_Type=TimeStamp
_Tn3270eSrvrStatsUpTime_Object=MibTableColumn
tn3270eSrvrStatsUpTime=_Tn3270eSrvrStatsUpTime_Object((1,3,6,1,2,1,34,8,1,3,1,2),_Tn3270eSrvrStatsUpTime_Type())
tn3270eSrvrStatsUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsUpTime.setStatus(_A)
_Tn3270eSrvrStatsMaxTerms_Type=Unsigned32
_Tn3270eSrvrStatsMaxTerms_Object=MibTableColumn
tn3270eSrvrStatsMaxTerms=_Tn3270eSrvrStatsMaxTerms_Object((1,3,6,1,2,1,34,8,1,3,1,3),_Tn3270eSrvrStatsMaxTerms_Type())
tn3270eSrvrStatsMaxTerms.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsMaxTerms.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsMaxTerms.setUnits(_P)
_Tn3270eSrvrStatsInUseTerms_Type=Gauge32
_Tn3270eSrvrStatsInUseTerms_Object=MibTableColumn
tn3270eSrvrStatsInUseTerms=_Tn3270eSrvrStatsInUseTerms_Object((1,3,6,1,2,1,34,8,1,3,1,4),_Tn3270eSrvrStatsInUseTerms_Type())
tn3270eSrvrStatsInUseTerms.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsInUseTerms.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsInUseTerms.setUnits(_P)
_Tn3270eSrvrStatsSpareTerms_Type=Gauge32
_Tn3270eSrvrStatsSpareTerms_Object=MibTableColumn
tn3270eSrvrStatsSpareTerms=_Tn3270eSrvrStatsSpareTerms_Object((1,3,6,1,2,1,34,8,1,3,1,5),_Tn3270eSrvrStatsSpareTerms_Type())
tn3270eSrvrStatsSpareTerms.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsSpareTerms.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsSpareTerms.setUnits(_P)
_Tn3270eSrvrStatsMaxPtrs_Type=Unsigned32
_Tn3270eSrvrStatsMaxPtrs_Object=MibTableColumn
tn3270eSrvrStatsMaxPtrs=_Tn3270eSrvrStatsMaxPtrs_Object((1,3,6,1,2,1,34,8,1,3,1,6),_Tn3270eSrvrStatsMaxPtrs_Type())
tn3270eSrvrStatsMaxPtrs.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsMaxPtrs.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsMaxPtrs.setUnits(_V)
_Tn3270eSrvrStatsInUsePtrs_Type=Gauge32
_Tn3270eSrvrStatsInUsePtrs_Object=MibTableColumn
tn3270eSrvrStatsInUsePtrs=_Tn3270eSrvrStatsInUsePtrs_Object((1,3,6,1,2,1,34,8,1,3,1,7),_Tn3270eSrvrStatsInUsePtrs_Type())
tn3270eSrvrStatsInUsePtrs.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsInUsePtrs.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsInUsePtrs.setUnits(_V)
_Tn3270eSrvrStatsSparePtrs_Type=Gauge32
_Tn3270eSrvrStatsSparePtrs_Object=MibTableColumn
tn3270eSrvrStatsSparePtrs=_Tn3270eSrvrStatsSparePtrs_Object((1,3,6,1,2,1,34,8,1,3,1,8),_Tn3270eSrvrStatsSparePtrs_Type())
tn3270eSrvrStatsSparePtrs.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsSparePtrs.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsSparePtrs.setUnits('Spare Printer Resources')
_Tn3270eSrvrStatsInConnects_Type=Counter32
_Tn3270eSrvrStatsInConnects_Object=MibTableColumn
tn3270eSrvrStatsInConnects=_Tn3270eSrvrStatsInConnects_Object((1,3,6,1,2,1,34,8,1,3,1,9),_Tn3270eSrvrStatsInConnects_Type())
tn3270eSrvrStatsInConnects.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsInConnects.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsInConnects.setUnits('connections')
_Tn3270eSrvrStatsConnResrceRejs_Type=Counter32
_Tn3270eSrvrStatsConnResrceRejs_Object=MibTableColumn
tn3270eSrvrStatsConnResrceRejs=_Tn3270eSrvrStatsConnResrceRejs_Object((1,3,6,1,2,1,34,8,1,3,1,10),_Tn3270eSrvrStatsConnResrceRejs_Type())
tn3270eSrvrStatsConnResrceRejs.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsConnResrceRejs.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsConnResrceRejs.setUnits(_W)
_Tn3270eSrvrStatsDisconnects_Type=Counter32
_Tn3270eSrvrStatsDisconnects_Object=MibTableColumn
tn3270eSrvrStatsDisconnects=_Tn3270eSrvrStatsDisconnects_Object((1,3,6,1,2,1,34,8,1,3,1,11),_Tn3270eSrvrStatsDisconnects_Type())
tn3270eSrvrStatsDisconnects.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsDisconnects.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsDisconnects.setUnits('disconnections')
_Tn3270eSrvrStatsHCInOctets_Type=Counter64
_Tn3270eSrvrStatsHCInOctets_Object=MibTableColumn
tn3270eSrvrStatsHCInOctets=_Tn3270eSrvrStatsHCInOctets_Object((1,3,6,1,2,1,34,8,1,3,1,12),_Tn3270eSrvrStatsHCInOctets_Type())
tn3270eSrvrStatsHCInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsHCInOctets.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsHCInOctets.setUnits(_I)
_Tn3270eSrvrStatsInOctets_Type=Counter32
_Tn3270eSrvrStatsInOctets_Object=MibTableColumn
tn3270eSrvrStatsInOctets=_Tn3270eSrvrStatsInOctets_Object((1,3,6,1,2,1,34,8,1,3,1,13),_Tn3270eSrvrStatsInOctets_Type())
tn3270eSrvrStatsInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsInOctets.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsInOctets.setUnits(_I)
_Tn3270eSrvrStatsHCOutOctets_Type=Counter64
_Tn3270eSrvrStatsHCOutOctets_Object=MibTableColumn
tn3270eSrvrStatsHCOutOctets=_Tn3270eSrvrStatsHCOutOctets_Object((1,3,6,1,2,1,34,8,1,3,1,14),_Tn3270eSrvrStatsHCOutOctets_Type())
tn3270eSrvrStatsHCOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsHCOutOctets.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsHCOutOctets.setUnits(_I)
_Tn3270eSrvrStatsOutOctets_Type=Counter32
_Tn3270eSrvrStatsOutOctets_Object=MibTableColumn
tn3270eSrvrStatsOutOctets=_Tn3270eSrvrStatsOutOctets_Object((1,3,6,1,2,1,34,8,1,3,1,15),_Tn3270eSrvrStatsOutOctets_Type())
tn3270eSrvrStatsOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsOutOctets.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsOutOctets.setUnits(_I)
_Tn3270eSrvrStatsConnErrorRejs_Type=Counter32
_Tn3270eSrvrStatsConnErrorRejs_Object=MibTableColumn
tn3270eSrvrStatsConnErrorRejs=_Tn3270eSrvrStatsConnErrorRejs_Object((1,3,6,1,2,1,34,8,1,3,1,16),_Tn3270eSrvrStatsConnErrorRejs_Type())
tn3270eSrvrStatsConnErrorRejs.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSrvrStatsConnErrorRejs.setStatus(_A)
if mibBuilder.loadTexts:tn3270eSrvrStatsConnErrorRejs.setUnits(_W)
_Tn3270eClientGroupTable_Object=MibTable
tn3270eClientGroupTable=_Tn3270eClientGroupTable_Object((1,3,6,1,2,1,34,8,1,4))
if mibBuilder.loadTexts:tn3270eClientGroupTable.setStatus(_A)
_Tn3270eClientGroupEntry_Object=MibTableRow
tn3270eClientGroupEntry=_Tn3270eClientGroupEntry_Object((1,3,6,1,2,1,34,8,1,4,1))
tn3270eClientGroupEntry.setIndexNames((0,_B,_G),(0,_B,_X),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:tn3270eClientGroupEntry.setStatus(_A)
class _Tn3270eClientGroupName_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Tn3270eClientGroupName_Type.__name__=_J
_Tn3270eClientGroupName_Object=MibTableColumn
tn3270eClientGroupName=_Tn3270eClientGroupName_Object((1,3,6,1,2,1,34,8,1,4,1,1),_Tn3270eClientGroupName_Type())
tn3270eClientGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eClientGroupName.setStatus(_A)
_Tn3270eClientGroupAddrType_Type=IANATn3270eAddrType
_Tn3270eClientGroupAddrType_Object=MibTableColumn
tn3270eClientGroupAddrType=_Tn3270eClientGroupAddrType_Object((1,3,6,1,2,1,34,8,1,4,1,2),_Tn3270eClientGroupAddrType_Type())
tn3270eClientGroupAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eClientGroupAddrType.setStatus(_A)
_Tn3270eClientGroupAddress_Type=IANATn3270eAddress
_Tn3270eClientGroupAddress_Object=MibTableColumn
tn3270eClientGroupAddress=_Tn3270eClientGroupAddress_Object((1,3,6,1,2,1,34,8,1,4,1,3),_Tn3270eClientGroupAddress_Type())
tn3270eClientGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eClientGroupAddress.setStatus(_A)
class _Tn3270eClientGroupSubnetMask_Type(IpAddress):defaultHexValue='FFFFFFFF'
_Tn3270eClientGroupSubnetMask_Type.__name__=_S
_Tn3270eClientGroupSubnetMask_Object=MibTableColumn
tn3270eClientGroupSubnetMask=_Tn3270eClientGroupSubnetMask_Object((1,3,6,1,2,1,34,8,1,4,1,4),_Tn3270eClientGroupSubnetMask_Type())
tn3270eClientGroupSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eClientGroupSubnetMask.setStatus(_A)
class _Tn3270eClientGroupPfxLength_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Tn3270eClientGroupPfxLength_Type.__name__=_F
_Tn3270eClientGroupPfxLength_Object=MibTableColumn
tn3270eClientGroupPfxLength=_Tn3270eClientGroupPfxLength_Object((1,3,6,1,2,1,34,8,1,4,1,5),_Tn3270eClientGroupPfxLength_Type())
tn3270eClientGroupPfxLength.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eClientGroupPfxLength.setStatus(_A)
if mibBuilder.loadTexts:tn3270eClientGroupPfxLength.setUnits('bits')
_Tn3270eClientGroupRowStatus_Type=RowStatus
_Tn3270eClientGroupRowStatus_Object=MibTableColumn
tn3270eClientGroupRowStatus=_Tn3270eClientGroupRowStatus_Object((1,3,6,1,2,1,34,8,1,4,1,6),_Tn3270eClientGroupRowStatus_Type())
tn3270eClientGroupRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eClientGroupRowStatus.setStatus(_A)
_Tn3270eResPoolTable_Object=MibTable
tn3270eResPoolTable=_Tn3270eResPoolTable_Object((1,3,6,1,2,1,34,8,1,5))
if mibBuilder.loadTexts:tn3270eResPoolTable.setStatus(_A)
_Tn3270eResPoolEntry_Object=MibTableRow
tn3270eResPoolEntry=_Tn3270eResPoolEntry_Object((1,3,6,1,2,1,34,8,1,5,1))
tn3270eResPoolEntry.setIndexNames((0,_B,_G),(0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:tn3270eResPoolEntry.setStatus(_A)
class _Tn3270eResPoolName_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Tn3270eResPoolName_Type.__name__=_J
_Tn3270eResPoolName_Object=MibTableColumn
tn3270eResPoolName=_Tn3270eResPoolName_Object((1,3,6,1,2,1,34,8,1,5,1,1),_Tn3270eResPoolName_Type())
tn3270eResPoolName.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eResPoolName.setStatus(_A)
_Tn3270eResPoolElementName_Type=SnaResourceName
_Tn3270eResPoolElementName_Object=MibTableColumn
tn3270eResPoolElementName=_Tn3270eResPoolElementName_Object((1,3,6,1,2,1,34,8,1,5,1,2),_Tn3270eResPoolElementName_Type())
tn3270eResPoolElementName.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eResPoolElementName.setStatus(_A)
_Tn3270eResPoolElementType_Type=IANATn3270ResourceType
_Tn3270eResPoolElementType_Object=MibTableColumn
tn3270eResPoolElementType=_Tn3270eResPoolElementType_Object((1,3,6,1,2,1,34,8,1,5,1,3),_Tn3270eResPoolElementType_Type())
tn3270eResPoolElementType.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eResPoolElementType.setStatus(_A)
_Tn3270eResPoolRowStatus_Type=RowStatus
_Tn3270eResPoolRowStatus_Object=MibTableColumn
tn3270eResPoolRowStatus=_Tn3270eResPoolRowStatus_Object((1,3,6,1,2,1,34,8,1,5,1,4),_Tn3270eResPoolRowStatus_Type())
tn3270eResPoolRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eResPoolRowStatus.setStatus(_A)
_Tn3270eSnaMapTable_Object=MibTable
tn3270eSnaMapTable=_Tn3270eSnaMapTable_Object((1,3,6,1,2,1,34,8,1,6))
if mibBuilder.loadTexts:tn3270eSnaMapTable.setStatus(_A)
_Tn3270eSnaMapEntry_Object=MibTableRow
tn3270eSnaMapEntry=_Tn3270eSnaMapEntry_Object((1,3,6,1,2,1,34,8,1,6,1))
tn3270eSnaMapEntry.setIndexNames((0,_B,_G),(0,_B,_c))
if mibBuilder.loadTexts:tn3270eSnaMapEntry.setStatus(_A)
_Tn3270eSnaMapSscpSuppliedName_Type=SnaResourceName
_Tn3270eSnaMapSscpSuppliedName_Object=MibTableColumn
tn3270eSnaMapSscpSuppliedName=_Tn3270eSnaMapSscpSuppliedName_Object((1,3,6,1,2,1,34,8,1,6,1,1),_Tn3270eSnaMapSscpSuppliedName_Type())
tn3270eSnaMapSscpSuppliedName.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eSnaMapSscpSuppliedName.setStatus(_A)
_Tn3270eSnaMapLocalName_Type=SnaResourceName
_Tn3270eSnaMapLocalName_Object=MibTableColumn
tn3270eSnaMapLocalName=_Tn3270eSnaMapLocalName_Object((1,3,6,1,2,1,34,8,1,6,1,2),_Tn3270eSnaMapLocalName_Type())
tn3270eSnaMapLocalName.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSnaMapLocalName.setStatus(_A)
_Tn3270eSnaMapPrimaryLuName_Type=SnaResourceName
_Tn3270eSnaMapPrimaryLuName_Object=MibTableColumn
tn3270eSnaMapPrimaryLuName=_Tn3270eSnaMapPrimaryLuName_Object((1,3,6,1,2,1,34,8,1,6,1,3),_Tn3270eSnaMapPrimaryLuName_Type())
tn3270eSnaMapPrimaryLuName.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eSnaMapPrimaryLuName.setStatus(_A)
_Tn3270eClientResMapTable_Object=MibTable
tn3270eClientResMapTable=_Tn3270eClientResMapTable_Object((1,3,6,1,2,1,34,8,1,7))
if mibBuilder.loadTexts:tn3270eClientResMapTable.setStatus(_A)
_Tn3270eClientResMapEntry_Object=MibTableRow
tn3270eClientResMapEntry=_Tn3270eClientResMapEntry_Object((1,3,6,1,2,1,34,8,1,7,1))
tn3270eClientResMapEntry.setIndexNames((0,_B,_G),(0,_B,_d),(0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:tn3270eClientResMapEntry.setStatus(_A)
class _Tn3270eClientResMapPoolName_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Tn3270eClientResMapPoolName_Type.__name__=_J
_Tn3270eClientResMapPoolName_Object=MibTableColumn
tn3270eClientResMapPoolName=_Tn3270eClientResMapPoolName_Object((1,3,6,1,2,1,34,8,1,7,1,1),_Tn3270eClientResMapPoolName_Type())
tn3270eClientResMapPoolName.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eClientResMapPoolName.setStatus(_A)
class _Tn3270eClientResMapClientGroupName_Type(Utf8String):subtypeSpec=Utf8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Tn3270eClientResMapClientGroupName_Type.__name__=_J
_Tn3270eClientResMapClientGroupName_Object=MibTableColumn
tn3270eClientResMapClientGroupName=_Tn3270eClientResMapClientGroupName_Object((1,3,6,1,2,1,34,8,1,7,1,2),_Tn3270eClientResMapClientGroupName_Type())
tn3270eClientResMapClientGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eClientResMapClientGroupName.setStatus(_A)
class _Tn3270eClientResMapClientPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tn3270eClientResMapClientPort_Type.__name__=_F
_Tn3270eClientResMapClientPort_Object=MibTableColumn
tn3270eClientResMapClientPort=_Tn3270eClientResMapClientPort_Object((1,3,6,1,2,1,34,8,1,7,1,3),_Tn3270eClientResMapClientPort_Type())
tn3270eClientResMapClientPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eClientResMapClientPort.setStatus(_A)
_Tn3270eClientResMapRowStatus_Type=RowStatus
_Tn3270eClientResMapRowStatus_Object=MibTableColumn
tn3270eClientResMapRowStatus=_Tn3270eClientResMapRowStatus_Object((1,3,6,1,2,1,34,8,1,7,1,4),_Tn3270eClientResMapRowStatus_Type())
tn3270eClientResMapRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tn3270eClientResMapRowStatus.setStatus(_A)
_Tn3270eResMapTable_Object=MibTable
tn3270eResMapTable=_Tn3270eResMapTable_Object((1,3,6,1,2,1,34,8,1,8))
if mibBuilder.loadTexts:tn3270eResMapTable.setStatus(_A)
_Tn3270eResMapEntry_Object=MibTableRow
tn3270eResMapEntry=_Tn3270eResMapEntry_Object((1,3,6,1,2,1,34,8,1,8,1))
tn3270eResMapEntry.setIndexNames((0,_B,_G),(0,_B,_g))
if mibBuilder.loadTexts:tn3270eResMapEntry.setStatus(_A)
_Tn3270eResMapElementName_Type=SnaResourceName
_Tn3270eResMapElementName_Object=MibTableColumn
tn3270eResMapElementName=_Tn3270eResMapElementName_Object((1,3,6,1,2,1,34,8,1,8,1,1),_Tn3270eResMapElementName_Type())
tn3270eResMapElementName.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eResMapElementName.setStatus(_A)
_Tn3270eResMapAddrType_Type=IANATn3270eAddrType
_Tn3270eResMapAddrType_Object=MibTableColumn
tn3270eResMapAddrType=_Tn3270eResMapAddrType_Object((1,3,6,1,2,1,34,8,1,8,1,2),_Tn3270eResMapAddrType_Type())
tn3270eResMapAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eResMapAddrType.setStatus(_A)
_Tn3270eResMapAddress_Type=IANATn3270eAddress
_Tn3270eResMapAddress_Object=MibTableColumn
tn3270eResMapAddress=_Tn3270eResMapAddress_Object((1,3,6,1,2,1,34,8,1,8,1,3),_Tn3270eResMapAddress_Type())
tn3270eResMapAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eResMapAddress.setStatus(_A)
class _Tn3270eResMapPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tn3270eResMapPort_Type.__name__=_F
_Tn3270eResMapPort_Object=MibTableColumn
tn3270eResMapPort=_Tn3270eResMapPort_Object((1,3,6,1,2,1,34,8,1,8,1,4),_Tn3270eResMapPort_Type())
tn3270eResMapPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eResMapPort.setStatus(_A)
_Tn3270eResMapElementType_Type=IANATn3270ResourceType
_Tn3270eResMapElementType_Object=MibTableColumn
tn3270eResMapElementType=_Tn3270eResMapElementType_Object((1,3,6,1,2,1,34,8,1,8,1,5),_Tn3270eResMapElementType_Type())
tn3270eResMapElementType.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eResMapElementType.setStatus(_A)
_Tn3270eResMapSscpSuppliedName_Type=SnaResourceName
_Tn3270eResMapSscpSuppliedName_Object=MibTableColumn
tn3270eResMapSscpSuppliedName=_Tn3270eResMapSscpSuppliedName_Object((1,3,6,1,2,1,34,8,1,8,1,6),_Tn3270eResMapSscpSuppliedName_Type())
tn3270eResMapSscpSuppliedName.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eResMapSscpSuppliedName.setStatus(_A)
_Tn3270eTcpConnTable_Object=MibTable
tn3270eTcpConnTable=_Tn3270eTcpConnTable_Object((1,3,6,1,2,1,34,8,1,9))
if mibBuilder.loadTexts:tn3270eTcpConnTable.setStatus(_A)
_Tn3270eTcpConnEntry_Object=MibTableRow
tn3270eTcpConnEntry=_Tn3270eTcpConnEntry_Object((1,3,6,1,2,1,34,8,1,9,1))
tn3270eTcpConnEntry.setIndexNames((0,_B,_h),(0,_B,_i),(0,_B,_j),(0,_B,_k),(0,_B,_l),(0,_B,_m))
if mibBuilder.loadTexts:tn3270eTcpConnEntry.setStatus(_A)
_Tn3270eTcpConnRemAddrType_Type=IANATn3270eAddrType
_Tn3270eTcpConnRemAddrType_Object=MibTableColumn
tn3270eTcpConnRemAddrType=_Tn3270eTcpConnRemAddrType_Object((1,3,6,1,2,1,34,8,1,9,1,1),_Tn3270eTcpConnRemAddrType_Type())
tn3270eTcpConnRemAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eTcpConnRemAddrType.setStatus(_A)
_Tn3270eTcpConnRemAddress_Type=IANATn3270eAddress
_Tn3270eTcpConnRemAddress_Object=MibTableColumn
tn3270eTcpConnRemAddress=_Tn3270eTcpConnRemAddress_Object((1,3,6,1,2,1,34,8,1,9,1,2),_Tn3270eTcpConnRemAddress_Type())
tn3270eTcpConnRemAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eTcpConnRemAddress.setStatus(_A)
class _Tn3270eTcpConnRemPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tn3270eTcpConnRemPort_Type.__name__=_F
_Tn3270eTcpConnRemPort_Object=MibTableColumn
tn3270eTcpConnRemPort=_Tn3270eTcpConnRemPort_Object((1,3,6,1,2,1,34,8,1,9,1,3),_Tn3270eTcpConnRemPort_Type())
tn3270eTcpConnRemPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eTcpConnRemPort.setStatus(_A)
_Tn3270eTcpConnLocalAddrType_Type=IANATn3270eAddrType
_Tn3270eTcpConnLocalAddrType_Object=MibTableColumn
tn3270eTcpConnLocalAddrType=_Tn3270eTcpConnLocalAddrType_Object((1,3,6,1,2,1,34,8,1,9,1,4),_Tn3270eTcpConnLocalAddrType_Type())
tn3270eTcpConnLocalAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eTcpConnLocalAddrType.setStatus(_A)
_Tn3270eTcpConnLocalAddress_Type=IANATn3270eAddress
_Tn3270eTcpConnLocalAddress_Object=MibTableColumn
tn3270eTcpConnLocalAddress=_Tn3270eTcpConnLocalAddress_Object((1,3,6,1,2,1,34,8,1,9,1,5),_Tn3270eTcpConnLocalAddress_Type())
tn3270eTcpConnLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eTcpConnLocalAddress.setStatus(_A)
class _Tn3270eTcpConnLocalPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Tn3270eTcpConnLocalPort_Type.__name__=_F
_Tn3270eTcpConnLocalPort_Object=MibTableColumn
tn3270eTcpConnLocalPort=_Tn3270eTcpConnLocalPort_Object((1,3,6,1,2,1,34,8,1,9,1,6),_Tn3270eTcpConnLocalPort_Type())
tn3270eTcpConnLocalPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tn3270eTcpConnLocalPort.setStatus(_A)
class _Tn3270eTcpConnLastActivity_Type(TimeTicks):defaultValue=0
_Tn3270eTcpConnLastActivity_Type.__name__=_T
_Tn3270eTcpConnLastActivity_Object=MibTableColumn
tn3270eTcpConnLastActivity=_Tn3270eTcpConnLastActivity_Object((1,3,6,1,2,1,34,8,1,9,1,7),_Tn3270eTcpConnLastActivity_Type())
tn3270eTcpConnLastActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnLastActivity.setStatus(_A)
_Tn3270eTcpConnBytesIn_Type=Counter32
_Tn3270eTcpConnBytesIn_Object=MibTableColumn
tn3270eTcpConnBytesIn=_Tn3270eTcpConnBytesIn_Object((1,3,6,1,2,1,34,8,1,9,1,8),_Tn3270eTcpConnBytesIn_Type())
tn3270eTcpConnBytesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnBytesIn.setStatus(_A)
if mibBuilder.loadTexts:tn3270eTcpConnBytesIn.setUnits(_I)
_Tn3270eTcpConnBytesOut_Type=Counter32
_Tn3270eTcpConnBytesOut_Object=MibTableColumn
tn3270eTcpConnBytesOut=_Tn3270eTcpConnBytesOut_Object((1,3,6,1,2,1,34,8,1,9,1,9),_Tn3270eTcpConnBytesOut_Type())
tn3270eTcpConnBytesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnBytesOut.setStatus(_A)
if mibBuilder.loadTexts:tn3270eTcpConnBytesOut.setUnits(_I)
_Tn3270eTcpConnResourceElement_Type=SnaResourceName
_Tn3270eTcpConnResourceElement_Object=MibTableColumn
tn3270eTcpConnResourceElement=_Tn3270eTcpConnResourceElement_Object((1,3,6,1,2,1,34,8,1,9,1,10),_Tn3270eTcpConnResourceElement_Type())
tn3270eTcpConnResourceElement.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnResourceElement.setStatus(_A)
_Tn3270eTcpConnResourceType_Type=IANATn3270ResourceType
_Tn3270eTcpConnResourceType_Object=MibTableColumn
tn3270eTcpConnResourceType=_Tn3270eTcpConnResourceType_Object((1,3,6,1,2,1,34,8,1,9,1,11),_Tn3270eTcpConnResourceType_Type())
tn3270eTcpConnResourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnResourceType.setStatus(_A)
_Tn3270eTcpConnDeviceType_Type=IANATn3270DeviceType
_Tn3270eTcpConnDeviceType_Object=MibTableColumn
tn3270eTcpConnDeviceType=_Tn3270eTcpConnDeviceType_Object((1,3,6,1,2,1,34,8,1,9,1,12),_Tn3270eTcpConnDeviceType_Type())
tn3270eTcpConnDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnDeviceType.setStatus(_A)
_Tn3270eTcpConnFunctions_Type=IANATn3270Functions
_Tn3270eTcpConnFunctions_Object=MibTableColumn
tn3270eTcpConnFunctions=_Tn3270eTcpConnFunctions_Object((1,3,6,1,2,1,34,8,1,9,1,13),_Tn3270eTcpConnFunctions_Type())
tn3270eTcpConnFunctions.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnFunctions.setStatus(_A)
_Tn3270eTcpConnId_Type=Unsigned32
_Tn3270eTcpConnId_Object=MibTableColumn
tn3270eTcpConnId=_Tn3270eTcpConnId_Object((1,3,6,1,2,1,34,8,1,9,1,14),_Tn3270eTcpConnId_Type())
tn3270eTcpConnId.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnId.setStatus(_A)
_Tn3270eTcpConnClientIdFormat_Type=IANATn3270eClientType
_Tn3270eTcpConnClientIdFormat_Object=MibTableColumn
tn3270eTcpConnClientIdFormat=_Tn3270eTcpConnClientIdFormat_Object((1,3,6,1,2,1,34,8,1,9,1,15),_Tn3270eTcpConnClientIdFormat_Type())
tn3270eTcpConnClientIdFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnClientIdFormat.setStatus(_A)
class _Tn3270eTcpConnClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_Tn3270eTcpConnClientId_Type.__name__=_L
_Tn3270eTcpConnClientId_Object=MibTableColumn
tn3270eTcpConnClientId=_Tn3270eTcpConnClientId_Object((1,3,6,1,2,1,34,8,1,9,1,16),_Tn3270eTcpConnClientId_Type())
tn3270eTcpConnClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnClientId.setStatus(_A)
_Tn3270eTcpConnTraceData_Type=Tn3270eTraceData
_Tn3270eTcpConnTraceData_Object=MibTableColumn
tn3270eTcpConnTraceData=_Tn3270eTcpConnTraceData_Object((1,3,6,1,2,1,34,8,1,9,1,17),_Tn3270eTcpConnTraceData_Type())
tn3270eTcpConnTraceData.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnTraceData.setStatus(_A)
_Tn3270eTcpConnLogInfo_Type=IANATn3270eLogData
_Tn3270eTcpConnLogInfo_Object=MibTableColumn
tn3270eTcpConnLogInfo=_Tn3270eTcpConnLogInfo_Object((1,3,6,1,2,1,34,8,1,9,1,18),_Tn3270eTcpConnLogInfo_Type())
tn3270eTcpConnLogInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnLogInfo.setStatus(_A)
class _Tn3270eTcpConnLuLuBindImage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_Tn3270eTcpConnLuLuBindImage_Type.__name__=_L
_Tn3270eTcpConnLuLuBindImage_Object=MibTableColumn
tn3270eTcpConnLuLuBindImage=_Tn3270eTcpConnLuLuBindImage_Object((1,3,6,1,2,1,34,8,1,9,1,19),_Tn3270eTcpConnLuLuBindImage_Type())
tn3270eTcpConnLuLuBindImage.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnLuLuBindImage.setStatus(_A)
class _Tn3270eTcpConnSnaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_n,1),('noSluSession',2),('sscpLuSession',3),('luLuSession',4),('sscpLuSessionAndLuLuSession',5)))
_Tn3270eTcpConnSnaState_Type.__name__=_H
_Tn3270eTcpConnSnaState_Object=MibTableColumn
tn3270eTcpConnSnaState=_Tn3270eTcpConnSnaState_Object((1,3,6,1,2,1,34,8,1,9,1,20),_Tn3270eTcpConnSnaState_Type())
tn3270eTcpConnSnaState.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnSnaState.setStatus(_A)
class _Tn3270eTcpConnStateLastDiscReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_n,1),('hostSendsUnbind',2),('hostDontAcceptConnection',3),('outOfResource',4),('clientProtocolError',5),('invalidDeviceName',6),('deviceInUse',7),('inactivityTimeout',8),('hostNotResponding',9),('clientNotResponding',10),('serverClose',11),('sysreqLogoff',12),('serverSpecificHexCode',13)))
_Tn3270eTcpConnStateLastDiscReason_Type.__name__=_H
_Tn3270eTcpConnStateLastDiscReason_Object=MibTableColumn
tn3270eTcpConnStateLastDiscReason=_Tn3270eTcpConnStateLastDiscReason_Object((1,3,6,1,2,1,34,8,1,9,1,21),_Tn3270eTcpConnStateLastDiscReason_Type())
tn3270eTcpConnStateLastDiscReason.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnStateLastDiscReason.setStatus(_A)
class _Tn3270eTcpConnSrvrConfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Tn3270eTcpConnSrvrConfIndex_Type.__name__=_F
_Tn3270eTcpConnSrvrConfIndex_Object=MibTableColumn
tn3270eTcpConnSrvrConfIndex=_Tn3270eTcpConnSrvrConfIndex_Object((1,3,6,1,2,1,34,8,1,9,1,22),_Tn3270eTcpConnSrvrConfIndex_Type())
tn3270eTcpConnSrvrConfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnSrvrConfIndex.setStatus(_A)
_Tn3270eTcpConnActivationTime_Type=TimeStamp
_Tn3270eTcpConnActivationTime_Object=MibTableColumn
tn3270eTcpConnActivationTime=_Tn3270eTcpConnActivationTime_Object((1,3,6,1,2,1,34,8,1,9,1,23),_Tn3270eTcpConnActivationTime_Type())
tn3270eTcpConnActivationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270eTcpConnActivationTime.setStatus(_A)
_Tn3270eConfSpinLock_Type=TestAndIncr
_Tn3270eConfSpinLock_Object=MibScalar
tn3270eConfSpinLock=_Tn3270eConfSpinLock_Object((1,3,6,1,2,1,34,8,1,10),_Tn3270eConfSpinLock_Type())
tn3270eConfSpinLock.setMaxAccess('read-write')
if mibBuilder.loadTexts:tn3270eConfSpinLock.setStatus(_A)
_Tn3270eConformance_ObjectIdentity=ObjectIdentity
tn3270eConformance=_Tn3270eConformance_ObjectIdentity((1,3,6,1,2,1,34,8,3))
_Tn3270eGroups_ObjectIdentity=ObjectIdentity
tn3270eGroups=_Tn3270eGroups_ObjectIdentity((1,3,6,1,2,1,34,8,3,1))
_Tn3270eCompliances_ObjectIdentity=ObjectIdentity
tn3270eCompliances=_Tn3270eCompliances_ObjectIdentity((1,3,6,1,2,1,34,8,3,2))
tn3270eBasicGroup=ObjectGroup((1,3,6,1,2,1,34,8,3,1,1))
tn3270eBasicGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:tn3270eBasicGroup.setStatus(_A)
tn3270eSessionGroup=ObjectGroup((1,3,6,1,2,1,34,8,3,1,2))
tn3270eSessionGroup.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:tn3270eSessionGroup.setStatus(_A)
tn3270eResMapGroup=ObjectGroup((1,3,6,1,2,1,34,8,3,1,3))
tn3270eResMapGroup.setObjects(*((_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj)))
if mibBuilder.loadTexts:tn3270eResMapGroup.setStatus(_A)
tn3270eHiCapacityGroup=ObjectGroup((1,3,6,1,2,1,34,8,3,1,4))
tn3270eHiCapacityGroup.setObjects(*((_B,_Ak),(_B,_Al)))
if mibBuilder.loadTexts:tn3270eHiCapacityGroup.setStatus(_A)
tn3270eCompliance=ModuleCompliance((1,3,6,1,2,1,34,8,3,2,1))
tn3270eCompliance.setObjects(*((_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap)))
if mibBuilder.loadTexts:tn3270eCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SnaResourceName':SnaResourceName,'Tn3270eTraceData':Tn3270eTraceData,'tn3270eMIB':tn3270eMIB,'tn3270eNotifications':tn3270eNotifications,'tn3270eObjects':tn3270eObjects,'tn3270eSrvrConfTable':tn3270eSrvrConfTable,'tn3270eSrvrConfEntry':tn3270eSrvrConfEntry,_G:tn3270eSrvrConfIndex,_o:tn3270eSrvrConfInactivityTimeout,_p:tn3270eSrvrConfConnectivityChk,_q:tn3270eSrvrConfTmNopInactTime,_r:tn3270eSrvrConfTmNopInterval,_s:tn3270eSrvrFunctionsSupported,_t:tn3270eSrvrConfAdminStatus,_u:tn3270eSrvrConfOperStatus,_v:tn3270eSrvrConfSessionTermState,_w:tn3270eSrvrConfSrvrType,_x:tn3270eSrvrConfContact,_y:tn3270eSrvrConfRowStatus,_z:tn3270eSrvrConfLastActTime,_A0:tn3270eSrvrConfTmTimeout,'tn3270eSrvrPortTable':tn3270eSrvrPortTable,'tn3270eSrvrPortEntry':tn3270eSrvrPortEntry,_M:tn3270eSrvrPort,_N:tn3270eSrvrPortAddrType,_O:tn3270eSrvrPortAddress,_A1:tn3270eSrvrPortRowStatus,'tn3270eSrvrStatsTable':tn3270eSrvrStatsTable,'tn3270eSrvrStatsEntry':tn3270eSrvrStatsEntry,_A2:tn3270eSrvrStatsUpTime,_A3:tn3270eSrvrStatsMaxTerms,_A4:tn3270eSrvrStatsInUseTerms,_A5:tn3270eSrvrStatsSpareTerms,_A6:tn3270eSrvrStatsMaxPtrs,_A7:tn3270eSrvrStatsInUsePtrs,_A8:tn3270eSrvrStatsSparePtrs,_A9:tn3270eSrvrStatsInConnects,_AA:tn3270eSrvrStatsConnResrceRejs,_AB:tn3270eSrvrStatsDisconnects,_Ak:tn3270eSrvrStatsHCInOctets,_AC:tn3270eSrvrStatsInOctets,_Al:tn3270eSrvrStatsHCOutOctets,_AD:tn3270eSrvrStatsOutOctets,_AE:tn3270eSrvrStatsConnErrorRejs,'tn3270eClientGroupTable':tn3270eClientGroupTable,'tn3270eClientGroupEntry':tn3270eClientGroupEntry,_X:tn3270eClientGroupName,_Y:tn3270eClientGroupAddrType,_Z:tn3270eClientGroupAddress,_AF:tn3270eClientGroupSubnetMask,_AG:tn3270eClientGroupPfxLength,_AH:tn3270eClientGroupRowStatus,'tn3270eResPoolTable':tn3270eResPoolTable,'tn3270eResPoolEntry':tn3270eResPoolEntry,_a:tn3270eResPoolName,_b:tn3270eResPoolElementName,_AZ:tn3270eResPoolElementType,_Aa:tn3270eResPoolRowStatus,'tn3270eSnaMapTable':tn3270eSnaMapTable,'tn3270eSnaMapEntry':tn3270eSnaMapEntry,_c:tn3270eSnaMapSscpSuppliedName,_AI:tn3270eSnaMapLocalName,_AJ:tn3270eSnaMapPrimaryLuName,'tn3270eClientResMapTable':tn3270eClientResMapTable,'tn3270eClientResMapEntry':tn3270eClientResMapEntry,_d:tn3270eClientResMapPoolName,_e:tn3270eClientResMapClientGroupName,_f:tn3270eClientResMapClientPort,_Ab:tn3270eClientResMapRowStatus,'tn3270eResMapTable':tn3270eResMapTable,'tn3270eResMapEntry':tn3270eResMapEntry,_g:tn3270eResMapElementName,_AL:tn3270eResMapAddrType,_AM:tn3270eResMapAddress,_AN:tn3270eResMapPort,_AO:tn3270eResMapElementType,_AP:tn3270eResMapSscpSuppliedName,'tn3270eTcpConnTable':tn3270eTcpConnTable,'tn3270eTcpConnEntry':tn3270eTcpConnEntry,_h:tn3270eTcpConnRemAddrType,_i:tn3270eTcpConnRemAddress,_j:tn3270eTcpConnRemPort,_k:tn3270eTcpConnLocalAddrType,_l:tn3270eTcpConnLocalAddress,_m:tn3270eTcpConnLocalPort,_AQ:tn3270eTcpConnLastActivity,_AR:tn3270eTcpConnBytesIn,_AS:tn3270eTcpConnBytesOut,_AT:tn3270eTcpConnResourceElement,_AU:tn3270eTcpConnResourceType,_AV:tn3270eTcpConnDeviceType,_AW:tn3270eTcpConnFunctions,_Ac:tn3270eTcpConnId,_Ad:tn3270eTcpConnClientIdFormat,_Ae:tn3270eTcpConnClientId,_Af:tn3270eTcpConnTraceData,_Ag:tn3270eTcpConnLogInfo,_Ah:tn3270eTcpConnLuLuBindImage,_Ai:tn3270eTcpConnSnaState,_Aj:tn3270eTcpConnStateLastDiscReason,_AX:tn3270eTcpConnSrvrConfIndex,_AY:tn3270eTcpConnActivationTime,_AK:tn3270eConfSpinLock,'tn3270eConformance':tn3270eConformance,'tn3270eGroups':tn3270eGroups,_Am:tn3270eBasicGroup,_An:tn3270eSessionGroup,_Ao:tn3270eResMapGroup,_Ap:tn3270eHiCapacityGroup,'tn3270eCompliances':tn3270eCompliances,'tn3270eCompliance':tn3270eCompliance})