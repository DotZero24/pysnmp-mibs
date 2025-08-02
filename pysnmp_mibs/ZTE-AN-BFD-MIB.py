_J='zxAnBfdSessPerfEntry'
_I='not-accessible'
_H='zxAnBfdL3IfVlan'
_G='zxAnBfdSessApplicationType'
_F='read-write'
_E='TruthValue'
_D='ZTE-AN-BFD-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_E)
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnBfdMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,15))
_ZxAnBfdMibObjects_ObjectIdentity=ObjectIdentity
zxAnBfdMibObjects=_ZxAnBfdMibObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,15,1))
_ZxAnBfdSessTable_Object=MibTable
zxAnBfdSessTable=_ZxAnBfdSessTable_Object((1,3,6,1,4,1,3902,1015,15,1,20))
if mibBuilder.loadTexts:zxAnBfdSessTable.setStatus(_A)
_ZxAnBfdSessEntry_Object=MibTableRow
zxAnBfdSessEntry=_ZxAnBfdSessEntry_Object((1,3,6,1,4,1,3902,1015,15,1,20,1))
zxAnBfdSessEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:zxAnBfdSessEntry.setStatus(_A)
class _ZxAnBfdSessApplicationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('uaps',1))
_ZxAnBfdSessApplicationType_Type.__name__=_C
_ZxAnBfdSessApplicationType_Object=MibTableColumn
zxAnBfdSessApplicationType=_ZxAnBfdSessApplicationType_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,1),_ZxAnBfdSessApplicationType_Type())
zxAnBfdSessApplicationType.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnBfdSessApplicationType.setStatus(_A)
class _ZxAnBfdL3IfVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnBfdL3IfVlan_Type.__name__=_C
_ZxAnBfdL3IfVlan_Object=MibTableColumn
zxAnBfdL3IfVlan=_ZxAnBfdL3IfVlan_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,2),_ZxAnBfdL3IfVlan_Type())
zxAnBfdL3IfVlan.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnBfdL3IfVlan.setStatus(_A)
class _ZxAnBfdSessDiscriminator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZxAnBfdSessDiscriminator_Type.__name__=_C
_ZxAnBfdSessDiscriminator_Object=MibTableColumn
zxAnBfdSessDiscriminator=_ZxAnBfdSessDiscriminator_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,3),_ZxAnBfdSessDiscriminator_Type())
zxAnBfdSessDiscriminator.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessDiscriminator.setStatus(_A)
class _ZxAnBfdSessRemoteDiscr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZxAnBfdSessRemoteDiscr_Type.__name__=_C
_ZxAnBfdSessRemoteDiscr_Object=MibTableColumn
zxAnBfdSessRemoteDiscr=_ZxAnBfdSessRemoteDiscr_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,4),_ZxAnBfdSessRemoteDiscr_Type())
zxAnBfdSessRemoteDiscr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessRemoteDiscr.setStatus(_A)
class _ZxAnBfdSessUdpPort_Type(Integer32):defaultValue=0
_ZxAnBfdSessUdpPort_Type.__name__=_C
_ZxAnBfdSessUdpPort_Object=MibTableColumn
zxAnBfdSessUdpPort=_ZxAnBfdSessUdpPort_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,5),_ZxAnBfdSessUdpPort_Type())
zxAnBfdSessUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessUdpPort.setStatus(_A)
class _ZxAnBfdSessState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('adminDown',1),('down',2),('init',3),('up',4)))
_ZxAnBfdSessState_Type.__name__=_C
_ZxAnBfdSessState_Object=MibTableColumn
zxAnBfdSessState=_ZxAnBfdSessState_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,6),_ZxAnBfdSessState_Type())
zxAnBfdSessState.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessState.setStatus(_A)
class _ZxAnBfdSessDemandModeDesiredFlag_Type(TruthValue):defaultValue=2
_ZxAnBfdSessDemandModeDesiredFlag_Type.__name__=_E
_ZxAnBfdSessDemandModeDesiredFlag_Object=MibTableColumn
zxAnBfdSessDemandModeDesiredFlag=_ZxAnBfdSessDemandModeDesiredFlag_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,7),_ZxAnBfdSessDemandModeDesiredFlag_Type())
zxAnBfdSessDemandModeDesiredFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessDemandModeDesiredFlag.setStatus(_A)
class _ZxAnBfdSessEchoFuncModeDesiredFlag_Type(TruthValue):defaultValue=2
_ZxAnBfdSessEchoFuncModeDesiredFlag_Type.__name__=_E
_ZxAnBfdSessEchoFuncModeDesiredFlag_Object=MibTableColumn
zxAnBfdSessEchoFuncModeDesiredFlag=_ZxAnBfdSessEchoFuncModeDesiredFlag_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,8),_ZxAnBfdSessEchoFuncModeDesiredFlag_Type())
zxAnBfdSessEchoFuncModeDesiredFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessEchoFuncModeDesiredFlag.setStatus(_A)
class _ZxAnBfdSessLocalAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_ZxAnBfdSessLocalAddrType_Type.__name__=_C
_ZxAnBfdSessLocalAddrType_Object=MibTableColumn
zxAnBfdSessLocalAddrType=_ZxAnBfdSessLocalAddrType_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,9),_ZxAnBfdSessLocalAddrType_Type())
zxAnBfdSessLocalAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessLocalAddrType.setStatus(_A)
_ZxAnBfdSessLocalAddr_Type=InetAddress
_ZxAnBfdSessLocalAddr_Object=MibTableColumn
zxAnBfdSessLocalAddr=_ZxAnBfdSessLocalAddr_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,10),_ZxAnBfdSessLocalAddr_Type())
zxAnBfdSessLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessLocalAddr.setStatus(_A)
class _ZxAnBfdSessRemoteAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_ZxAnBfdSessRemoteAddrType_Type.__name__=_C
_ZxAnBfdSessRemoteAddrType_Object=MibTableColumn
zxAnBfdSessRemoteAddrType=_ZxAnBfdSessRemoteAddrType_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,11),_ZxAnBfdSessRemoteAddrType_Type())
zxAnBfdSessRemoteAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessRemoteAddrType.setStatus(_A)
_ZxAnBfdSessRemoteAddr_Type=InetAddress
_ZxAnBfdSessRemoteAddr_Object=MibTableColumn
zxAnBfdSessRemoteAddr=_ZxAnBfdSessRemoteAddr_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,12),_ZxAnBfdSessRemoteAddr_Type())
zxAnBfdSessRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessRemoteAddr.setStatus(_A)
_ZxAnBfdSessDesiredMinTxInterval_Type=Integer32
_ZxAnBfdSessDesiredMinTxInterval_Object=MibTableColumn
zxAnBfdSessDesiredMinTxInterval=_ZxAnBfdSessDesiredMinTxInterval_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,13),_ZxAnBfdSessDesiredMinTxInterval_Type())
zxAnBfdSessDesiredMinTxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnBfdSessDesiredMinTxInterval.setStatus(_A)
_ZxAnBfdSessRequiredMinRxInterval_Type=Integer32
_ZxAnBfdSessRequiredMinRxInterval_Object=MibTableColumn
zxAnBfdSessRequiredMinRxInterval=_ZxAnBfdSessRequiredMinRxInterval_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,14),_ZxAnBfdSessRequiredMinRxInterval_Type())
zxAnBfdSessRequiredMinRxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnBfdSessRequiredMinRxInterval.setStatus(_A)
_ZxAnBfdSessDetectMult_Type=Integer32
_ZxAnBfdSessDetectMult_Object=MibTableColumn
zxAnBfdSessDetectMult=_ZxAnBfdSessDetectMult_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,15),_ZxAnBfdSessDetectMult_Type())
zxAnBfdSessDetectMult.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnBfdSessDetectMult.setStatus(_A)
class _ZxAnBfdSessDownDiag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noDiagnostic',1),('controlDetectionTimeExpired',2),('echoFunctionFailed',3),('neighborSignaledSessionDown',4),('forwardingPlaneReset',5),('pathDown',6),('concatenatedPathDown',7),('administrativelyDown',8),('reverseConcatenatedPathDown',9)))
_ZxAnBfdSessDownDiag_Type.__name__=_C
_ZxAnBfdSessDownDiag_Object=MibTableColumn
zxAnBfdSessDownDiag=_ZxAnBfdSessDownDiag_Object((1,3,6,1,4,1,3902,1015,15,1,20,1,16),_ZxAnBfdSessDownDiag_Type())
zxAnBfdSessDownDiag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessDownDiag.setStatus(_A)
_ZxAnBfdSessPerfTable_Object=MibTable
zxAnBfdSessPerfTable=_ZxAnBfdSessPerfTable_Object((1,3,6,1,4,1,3902,1015,15,1,21))
if mibBuilder.loadTexts:zxAnBfdSessPerfTable.setStatus(_A)
_ZxAnBfdSessPerfEntry_Object=MibTableRow
zxAnBfdSessPerfEntry=_ZxAnBfdSessPerfEntry_Object((1,3,6,1,4,1,3902,1015,15,1,21,1))
if mibBuilder.loadTexts:zxAnBfdSessPerfEntry.setStatus(_A)
_ZxAnBfdSessPerfPktIn_Type=Counter32
_ZxAnBfdSessPerfPktIn_Object=MibTableColumn
zxAnBfdSessPerfPktIn=_ZxAnBfdSessPerfPktIn_Object((1,3,6,1,4,1,3902,1015,15,1,21,1,1),_ZxAnBfdSessPerfPktIn_Type())
zxAnBfdSessPerfPktIn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessPerfPktIn.setStatus(_A)
_ZxAnBfdSessPerfPktOut_Type=Counter32
_ZxAnBfdSessPerfPktOut_Object=MibTableColumn
zxAnBfdSessPerfPktOut=_ZxAnBfdSessPerfPktOut_Object((1,3,6,1,4,1,3902,1015,15,1,21,1,2),_ZxAnBfdSessPerfPktOut_Type())
zxAnBfdSessPerfPktOut.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessPerfPktOut.setStatus(_A)
_ZxAnBfdSessPerfUpTime_Type=TimeStamp
_ZxAnBfdSessPerfUpTime_Object=MibTableColumn
zxAnBfdSessPerfUpTime=_ZxAnBfdSessPerfUpTime_Object((1,3,6,1,4,1,3902,1015,15,1,21,1,3),_ZxAnBfdSessPerfUpTime_Type())
zxAnBfdSessPerfUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessPerfUpTime.setStatus(_A)
_ZxAnBfdSessPerfDownTime_Type=TimeStamp
_ZxAnBfdSessPerfDownTime_Object=MibTableColumn
zxAnBfdSessPerfDownTime=_ZxAnBfdSessPerfDownTime_Object((1,3,6,1,4,1,3902,1015,15,1,21,1,4),_ZxAnBfdSessPerfDownTime_Type())
zxAnBfdSessPerfDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnBfdSessPerfDownTime.setStatus(_A)
zxAnBfdSessEntry.registerAugmentions((_D,_J))
zxAnBfdSessPerfEntry.setIndexNames(*zxAnBfdSessEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'zxAnBfdMib':zxAnBfdMib,'zxAnBfdMibObjects':zxAnBfdMibObjects,'zxAnBfdSessTable':zxAnBfdSessTable,'zxAnBfdSessEntry':zxAnBfdSessEntry,_G:zxAnBfdSessApplicationType,_H:zxAnBfdL3IfVlan,'zxAnBfdSessDiscriminator':zxAnBfdSessDiscriminator,'zxAnBfdSessRemoteDiscr':zxAnBfdSessRemoteDiscr,'zxAnBfdSessUdpPort':zxAnBfdSessUdpPort,'zxAnBfdSessState':zxAnBfdSessState,'zxAnBfdSessDemandModeDesiredFlag':zxAnBfdSessDemandModeDesiredFlag,'zxAnBfdSessEchoFuncModeDesiredFlag':zxAnBfdSessEchoFuncModeDesiredFlag,'zxAnBfdSessLocalAddrType':zxAnBfdSessLocalAddrType,'zxAnBfdSessLocalAddr':zxAnBfdSessLocalAddr,'zxAnBfdSessRemoteAddrType':zxAnBfdSessRemoteAddrType,'zxAnBfdSessRemoteAddr':zxAnBfdSessRemoteAddr,'zxAnBfdSessDesiredMinTxInterval':zxAnBfdSessDesiredMinTxInterval,'zxAnBfdSessRequiredMinRxInterval':zxAnBfdSessRequiredMinRxInterval,'zxAnBfdSessDetectMult':zxAnBfdSessDetectMult,'zxAnBfdSessDownDiag':zxAnBfdSessDownDiag,'zxAnBfdSessPerfTable':zxAnBfdSessPerfTable,_J:zxAnBfdSessPerfEntry,'zxAnBfdSessPerfPktIn':zxAnBfdSessPerfPktIn,'zxAnBfdSessPerfPktOut':zxAnBfdSessPerfPktOut,'zxAnBfdSessPerfUpTime':zxAnBfdSessPerfUpTime,'zxAnBfdSessPerfDownTime':zxAnBfdSessPerfDownTime})