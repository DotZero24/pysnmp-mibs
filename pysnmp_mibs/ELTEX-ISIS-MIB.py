_i='eltexIsisLSPID'
_h='eltexIsisLSPLevel'
_g='eltexIsisISAdjIPAddrIndex'
_f='eltexIsisISAdjAreaAddrIndex'
_e='failed'
_d='initializing'
_c='EltexIsisWideMetric'
_b='EltexIsisHelloPaddingAction'
_a='level2'
_Z='level1'
_Y='eltexIsisRouterLevel'
_X='eltexIsisRouterSysID'
_W='EltexIsisMetricStyle'
_V='eltexIsisSysLevelIndex'
_U='eltexIsisNetAddr'
_T='InetAddress'
_S='seconds'
_R='eltexIsisCircLevelIndex'
_Q='EltexIsisAdminState'
_P='level2IS'
_O='level1IS'
_N='reserved'
_M='eltexIsisISAdjIndex'
_L='TruthValue'
_K='OctetString'
_J='eltexIsisCircIfindex'
_I='read-create'
_H='not-accessible'
_G='eltexIsisSysInstance'
_F='Integer32'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='ELTEX-ISIS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_T,'InetAddressPrefixLength','InetAddressType','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp',_L)
eltexIsisMIB=ModuleIdentity((1,3,6,1,4,1,35265,55))
class EltexIsisSystemID(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class EltexIsisAdminState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
class EltexNETAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
class EltexIsisOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('operStatusUp',1),('operStatusDown',2),('operStatusGoingUp',3),('operStatusGoingDown',4),('operStatusActFailed',5)))
class EltexIsisISLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('area',1),('domain',2)))
class EltexIsisLinkStatePDUID(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class EltexIsisISPriority(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
class EltexIsisMetricStyle(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('narrow',1),('wide',2),('both',3)))
class EltexIsisWideMetric(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
class EltexIsisAuthType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('simplePassword',1),('hmac-md5',2)))
class EltexIsisHelloPaddingAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('enabled',1),('adaptive',2)))
_EltexIsisObjects_ObjectIdentity=ObjectIdentity
eltexIsisObjects=_EltexIsisObjects_ObjectIdentity((1,3,6,1,4,1,35265,55,1))
_EltexIsisSystem_ObjectIdentity=ObjectIdentity
eltexIsisSystem=_EltexIsisSystem_ObjectIdentity((1,3,6,1,4,1,35265,55,1,1))
_EltexIsisSysTable_Object=MibTable
eltexIsisSysTable=_EltexIsisSysTable_Object((1,3,6,1,4,1,35265,55,1,1,1))
if mibBuilder.loadTexts:eltexIsisSysTable.setStatus(_A)
_EltexIsisSysEntry_Object=MibTableRow
eltexIsisSysEntry=_EltexIsisSysEntry_Object((1,3,6,1,4,1,35265,55,1,1,1,1))
eltexIsisSysEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:eltexIsisSysEntry.setStatus(_A)
class _EltexIsisSysInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltexIsisSysInstance_Type.__name__=_F
_EltexIsisSysInstance_Object=MibTableColumn
eltexIsisSysInstance=_EltexIsisSysInstance_Object((1,3,6,1,4,1,35265,55,1,1,1,1,1),_EltexIsisSysInstance_Type())
eltexIsisSysInstance.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexIsisSysInstance.setStatus(_A)
class _EltexIsisSysType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),('level1L2IS',3)))
_EltexIsisSysType_Type.__name__=_F
_EltexIsisSysType_Object=MibTableColumn
eltexIsisSysType=_EltexIsisSysType_Object((1,3,6,1,4,1,35265,55,1,1,1,1,2),_EltexIsisSysType_Type())
eltexIsisSysType.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexIsisSysType.setStatus(_A)
_EltexIsisSysID_Type=EltexIsisSystemID
_EltexIsisSysID_Object=MibTableColumn
eltexIsisSysID=_EltexIsisSysID_Object((1,3,6,1,4,1,35265,55,1,1,1,1,3),_EltexIsisSysID_Type())
eltexIsisSysID.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisSysID.setStatus(_A)
class _EltexIsisSysAdminState_Type(EltexIsisAdminState):defaultValue=2
_EltexIsisSysAdminState_Type.__name__=_Q
_EltexIsisSysAdminState_Object=MibTableColumn
eltexIsisSysAdminState=_EltexIsisSysAdminState_Object((1,3,6,1,4,1,35265,55,1,1,1,1,4),_EltexIsisSysAdminState_Type())
eltexIsisSysAdminState.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexIsisSysAdminState.setStatus(_A)
_EltexIsisSysOperState_Type=EltexIsisOperStatus
_EltexIsisSysOperState_Object=MibTableColumn
eltexIsisSysOperState=_EltexIsisSysOperState_Object((1,3,6,1,4,1,35265,55,1,1,1,1,5),_EltexIsisSysOperState_Type())
eltexIsisSysOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisSysOperState.setStatus(_A)
_EltexIsisSysRowStatus_Type=RowStatus
_EltexIsisSysRowStatus_Object=MibTableColumn
eltexIsisSysRowStatus=_EltexIsisSysRowStatus_Object((1,3,6,1,4,1,35265,55,1,1,1,1,6),_EltexIsisSysRowStatus_Type())
eltexIsisSysRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexIsisSysRowStatus.setStatus(_A)
class _EltexIsisSysMaxAge_Type(Unsigned32):defaultValue=1200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(350,65535))
_EltexIsisSysMaxAge_Type.__name__=_E
_EltexIsisSysMaxAge_Object=MibTableColumn
eltexIsisSysMaxAge=_EltexIsisSysMaxAge_Object((1,3,6,1,4,1,35265,55,1,1,1,1,7),_EltexIsisSysMaxAge_Type())
eltexIsisSysMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisSysMaxAge.setStatus(_A)
class _EltexIsisSysMaxLSPGenInt_Type(Unsigned32):defaultValue=900;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65235))
_EltexIsisSysMaxLSPGenInt_Type.__name__=_E
_EltexIsisSysMaxLSPGenInt_Object=MibTableColumn
eltexIsisSysMaxLSPGenInt=_EltexIsisSysMaxLSPGenInt_Object((1,3,6,1,4,1,35265,55,1,1,1,1,8),_EltexIsisSysMaxLSPGenInt_Type())
eltexIsisSysMaxLSPGenInt.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisSysMaxLSPGenInt.setStatus(_A)
class _EltexIsisSysCalcMaxDelay_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EltexIsisSysCalcMaxDelay_Type.__name__=_E
_EltexIsisSysCalcMaxDelay_Object=MibTableColumn
eltexIsisSysCalcMaxDelay=_EltexIsisSysCalcMaxDelay_Object((1,3,6,1,4,1,35265,55,1,1,1,1,9),_EltexIsisSysCalcMaxDelay_Type())
eltexIsisSysCalcMaxDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisSysCalcMaxDelay.setStatus(_A)
class _EltexIsisSysCalcThrshUpdStart_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EltexIsisSysCalcThrshUpdStart_Type.__name__=_E
_EltexIsisSysCalcThrshUpdStart_Object=MibTableColumn
eltexIsisSysCalcThrshUpdStart=_EltexIsisSysCalcThrshUpdStart_Object((1,3,6,1,4,1,35265,55,1,1,1,1,10),_EltexIsisSysCalcThrshUpdStart_Type())
eltexIsisSysCalcThrshUpdStart.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisSysCalcThrshUpdStart.setStatus(_A)
class _EltexIsisSysCalcThrshUpdRestart_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EltexIsisSysCalcThrshUpdRestart_Type.__name__=_E
_EltexIsisSysCalcThrshUpdRestart_Object=MibTableColumn
eltexIsisSysCalcThrshUpdRestart=_EltexIsisSysCalcThrshUpdRestart_Object((1,3,6,1,4,1,35265,55,1,1,1,1,11),_EltexIsisSysCalcThrshUpdRestart_Type())
eltexIsisSysCalcThrshUpdRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisSysCalcThrshUpdRestart.setStatus(_A)
class _EltexIsisSysCalcThrshRestartLimit_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EltexIsisSysCalcThrshRestartLimit_Type.__name__=_E
_EltexIsisSysCalcThrshRestartLimit_Object=MibTableColumn
eltexIsisSysCalcThrshRestartLimit=_EltexIsisSysCalcThrshRestartLimit_Object((1,3,6,1,4,1,35265,55,1,1,1,1,12),_EltexIsisSysCalcThrshRestartLimit_Type())
eltexIsisSysCalcThrshRestartLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisSysCalcThrshRestartLimit.setStatus(_A)
class _EltexIsisSysHostNameDynamic_Type(TruthValue):defaultValue=1
_EltexIsisSysHostNameDynamic_Type.__name__=_L
_EltexIsisSysHostNameDynamic_Object=MibTableColumn
eltexIsisSysHostNameDynamic=_EltexIsisSysHostNameDynamic_Object((1,3,6,1,4,1,35265,55,1,1,1,1,13),_EltexIsisSysHostNameDynamic_Type())
eltexIsisSysHostNameDynamic.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisSysHostNameDynamic.setStatus(_A)
_EltexIsisNetAddrTable_Object=MibTable
eltexIsisNetAddrTable=_EltexIsisNetAddrTable_Object((1,3,6,1,4,1,35265,55,1,1,2))
if mibBuilder.loadTexts:eltexIsisNetAddrTable.setStatus(_A)
_EltexIsisNetAddrEntry_Object=MibTableRow
eltexIsisNetAddrEntry=_EltexIsisNetAddrEntry_Object((1,3,6,1,4,1,35265,55,1,1,2,1))
eltexIsisNetAddrEntry.setIndexNames((0,_B,_G),(0,_B,_U))
if mibBuilder.loadTexts:eltexIsisNetAddrEntry.setStatus(_A)
_EltexIsisNetAddr_Type=EltexNETAddress
_EltexIsisNetAddr_Object=MibTableColumn
eltexIsisNetAddr=_EltexIsisNetAddr_Object((1,3,6,1,4,1,35265,55,1,1,2,1,1),_EltexIsisNetAddr_Type())
eltexIsisNetAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexIsisNetAddr.setStatus(_A)
_EltexIsisNetAddrRowStatus_Type=RowStatus
_EltexIsisNetAddrRowStatus_Object=MibTableColumn
eltexIsisNetAddrRowStatus=_EltexIsisNetAddrRowStatus_Object((1,3,6,1,4,1,35265,55,1,1,2,1,2),_EltexIsisNetAddrRowStatus_Type())
eltexIsisNetAddrRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexIsisNetAddrRowStatus.setStatus(_A)
_EltexIsisSysLevelTable_Object=MibTable
eltexIsisSysLevelTable=_EltexIsisSysLevelTable_Object((1,3,6,1,4,1,35265,55,1,1,3))
if mibBuilder.loadTexts:eltexIsisSysLevelTable.setStatus(_A)
_EltexIsisSysLevelEntry_Object=MibTableRow
eltexIsisSysLevelEntry=_EltexIsisSysLevelEntry_Object((1,3,6,1,4,1,35265,55,1,1,3,1))
eltexIsisSysLevelEntry.setIndexNames((0,_B,_G),(0,_B,_V))
if mibBuilder.loadTexts:eltexIsisSysLevelEntry.setStatus(_A)
class _EltexIsisSysLevelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_EltexIsisSysLevelIndex_Type.__name__=_F
_EltexIsisSysLevelIndex_Object=MibTableColumn
eltexIsisSysLevelIndex=_EltexIsisSysLevelIndex_Object((1,3,6,1,4,1,35265,55,1,1,3,1,1),_EltexIsisSysLevelIndex_Type())
eltexIsisSysLevelIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexIsisSysLevelIndex.setStatus(_A)
class _EltexIsisSysLevelMinLSPGenInt_Type(Unsigned32):defaultValue=30000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,65535000))
_EltexIsisSysLevelMinLSPGenInt_Type.__name__=_E
_EltexIsisSysLevelMinLSPGenInt_Object=MibTableColumn
eltexIsisSysLevelMinLSPGenInt=_EltexIsisSysLevelMinLSPGenInt_Object((1,3,6,1,4,1,35265,55,1,1,3,1,2),_EltexIsisSysLevelMinLSPGenInt_Type())
eltexIsisSysLevelMinLSPGenInt.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisSysLevelMinLSPGenInt.setStatus(_A)
class _EltexIsisSysLevelMetricStyle_Type(EltexIsisMetricStyle):defaultValue=3
_EltexIsisSysLevelMetricStyle_Type.__name__=_W
_EltexIsisSysLevelMetricStyle_Object=MibTableColumn
eltexIsisSysLevelMetricStyle=_EltexIsisSysLevelMetricStyle_Object((1,3,6,1,4,1,35265,55,1,1,3,1,3),_EltexIsisSysLevelMetricStyle_Type())
eltexIsisSysLevelMetricStyle.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisSysLevelMetricStyle.setStatus(_A)
_EltexIsisSysLevelAuthType_Type=EltexIsisAuthType
_EltexIsisSysLevelAuthType_Object=MibTableColumn
eltexIsisSysLevelAuthType=_EltexIsisSysLevelAuthType_Object((1,3,6,1,4,1,35265,55,1,1,3,1,4),_EltexIsisSysLevelAuthType_Type())
eltexIsisSysLevelAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisSysLevelAuthType.setStatus(_A)
class _EltexIsisSysLevelAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_EltexIsisSysLevelAuthKey_Type.__name__=_K
_EltexIsisSysLevelAuthKey_Object=MibTableColumn
eltexIsisSysLevelAuthKey=_EltexIsisSysLevelAuthKey_Object((1,3,6,1,4,1,35265,55,1,1,3,1,5),_EltexIsisSysLevelAuthKey_Type())
eltexIsisSysLevelAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisSysLevelAuthKey.setStatus(_A)
class _EltexIsisSysLevelAuthKeyChain_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EltexIsisSysLevelAuthKeyChain_Type.__name__=_K
_EltexIsisSysLevelAuthKeyChain_Object=MibTableColumn
eltexIsisSysLevelAuthKeyChain=_EltexIsisSysLevelAuthKeyChain_Object((1,3,6,1,4,1,35265,55,1,1,3,1,6),_EltexIsisSysLevelAuthKeyChain_Type())
eltexIsisSysLevelAuthKeyChain.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisSysLevelAuthKeyChain.setStatus(_A)
class _EltexIsisSysLevelOrigLSPBuffSize_Type(Unsigned32):defaultValue=1500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,9000))
_EltexIsisSysLevelOrigLSPBuffSize_Type.__name__=_E
_EltexIsisSysLevelOrigLSPBuffSize_Object=MibTableColumn
eltexIsisSysLevelOrigLSPBuffSize=_EltexIsisSysLevelOrigLSPBuffSize_Object((1,3,6,1,4,1,35265,55,1,1,3,1,7),_EltexIsisSysLevelOrigLSPBuffSize_Type())
eltexIsisSysLevelOrigLSPBuffSize.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisSysLevelOrigLSPBuffSize.setStatus(_A)
_EltexIsisRouterTable_Object=MibTable
eltexIsisRouterTable=_EltexIsisRouterTable_Object((1,3,6,1,4,1,35265,55,1,1,5))
if mibBuilder.loadTexts:eltexIsisRouterTable.setStatus(_A)
_EltexIsisRouterEntry_Object=MibTableRow
eltexIsisRouterEntry=_EltexIsisRouterEntry_Object((1,3,6,1,4,1,35265,55,1,1,5,1))
eltexIsisRouterEntry.setIndexNames((0,_B,_G),(0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:eltexIsisRouterEntry.setStatus(_A)
_EltexIsisRouterSysID_Type=EltexIsisSystemID
_EltexIsisRouterSysID_Object=MibTableColumn
eltexIsisRouterSysID=_EltexIsisRouterSysID_Object((1,3,6,1,4,1,35265,55,1,1,5,1,1),_EltexIsisRouterSysID_Type())
eltexIsisRouterSysID.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexIsisRouterSysID.setStatus(_A)
_EltexIsisRouterLevel_Type=EltexIsisISLevel
_EltexIsisRouterLevel_Object=MibTableColumn
eltexIsisRouterLevel=_EltexIsisRouterLevel_Object((1,3,6,1,4,1,35265,55,1,1,5,1,2),_EltexIsisRouterLevel_Type())
eltexIsisRouterLevel.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexIsisRouterLevel.setStatus(_A)
_EltexIsisRouterHostName_Type=SnmpAdminString
_EltexIsisRouterHostName_Object=MibTableColumn
eltexIsisRouterHostName=_EltexIsisRouterHostName_Object((1,3,6,1,4,1,35265,55,1,1,5,1,3),_EltexIsisRouterHostName_Type())
eltexIsisRouterHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisRouterHostName.setStatus(_A)
_EltexIsisCirc_ObjectIdentity=ObjectIdentity
eltexIsisCirc=_EltexIsisCirc_ObjectIdentity((1,3,6,1,4,1,35265,55,1,2))
_EltexIsisCircTable_Object=MibTable
eltexIsisCircTable=_EltexIsisCircTable_Object((1,3,6,1,4,1,35265,55,1,2,1))
if mibBuilder.loadTexts:eltexIsisCircTable.setStatus(_A)
_EltexIsisCircEntry_Object=MibTableRow
eltexIsisCircEntry=_EltexIsisCircEntry_Object((1,3,6,1,4,1,35265,55,1,2,1,1))
eltexIsisCircEntry.setIndexNames((0,_B,_G),(0,_B,_J))
if mibBuilder.loadTexts:eltexIsisCircEntry.setStatus(_A)
_EltexIsisCircIfindex_Type=InterfaceIndex
_EltexIsisCircIfindex_Object=MibTableColumn
eltexIsisCircIfindex=_EltexIsisCircIfindex_Object((1,3,6,1,4,1,35265,55,1,2,1,1,1),_EltexIsisCircIfindex_Type())
eltexIsisCircIfindex.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexIsisCircIfindex.setStatus(_A)
_EltexIsisCircRowStatus_Type=RowStatus
_EltexIsisCircRowStatus_Object=MibTableColumn
eltexIsisCircRowStatus=_EltexIsisCircRowStatus_Object((1,3,6,1,4,1,35265,55,1,2,1,1,2),_EltexIsisCircRowStatus_Type())
eltexIsisCircRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexIsisCircRowStatus.setStatus(_A)
class _EltexIsisCircAdminState_Type(EltexIsisAdminState):defaultValue=2
_EltexIsisCircAdminState_Type.__name__=_Q
_EltexIsisCircAdminState_Object=MibTableColumn
eltexIsisCircAdminState=_EltexIsisCircAdminState_Object((1,3,6,1,4,1,35265,55,1,2,1,1,3),_EltexIsisCircAdminState_Type())
eltexIsisCircAdminState.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexIsisCircAdminState.setStatus(_A)
_EltexIsisCircOperState_Type=EltexIsisOperStatus
_EltexIsisCircOperState_Object=MibTableColumn
eltexIsisCircOperState=_EltexIsisCircOperState_Object((1,3,6,1,4,1,35265,55,1,2,1,1,4),_EltexIsisCircOperState_Type())
eltexIsisCircOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisCircOperState.setStatus(_A)
class _EltexIsisCircLevel_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),(_Z,1),(_a,2),('level1L2',3)))
_EltexIsisCircLevel_Type.__name__=_F
_EltexIsisCircLevel_Object=MibTableColumn
eltexIsisCircLevel=_EltexIsisCircLevel_Object((1,3,6,1,4,1,35265,55,1,2,1,1,5),_EltexIsisCircLevel_Type())
eltexIsisCircLevel.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexIsisCircLevel.setStatus(_A)
class _EltexIsisCircPassiveCircuit_Type(TruthValue):defaultValue=2
_EltexIsisCircPassiveCircuit_Type.__name__=_L
_EltexIsisCircPassiveCircuit_Object=MibTableColumn
eltexIsisCircPassiveCircuit=_EltexIsisCircPassiveCircuit_Object((1,3,6,1,4,1,35265,55,1,2,1,1,6),_EltexIsisCircPassiveCircuit_Type())
eltexIsisCircPassiveCircuit.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexIsisCircPassiveCircuit.setStatus(_A)
class _EltexIsisCircPtToPt_Type(TruthValue):defaultValue=2
_EltexIsisCircPtToPt_Type.__name__=_L
_EltexIsisCircPtToPt_Object=MibTableColumn
eltexIsisCircPtToPt=_EltexIsisCircPtToPt_Object((1,3,6,1,4,1,35265,55,1,2,1,1,7),_EltexIsisCircPtToPt_Type())
eltexIsisCircPtToPt.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisCircPtToPt.setStatus(_A)
class _EltexIsisCircHelloPadding_Type(EltexIsisHelloPaddingAction):defaultValue=1
_EltexIsisCircHelloPadding_Type.__name__=_b
_EltexIsisCircHelloPadding_Object=MibTableColumn
eltexIsisCircHelloPadding=_EltexIsisCircHelloPadding_Object((1,3,6,1,4,1,35265,55,1,2,1,1,8),_EltexIsisCircHelloPadding_Type())
eltexIsisCircHelloPadding.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisCircHelloPadding.setStatus(_A)
class _EltexIsisCircPDUBuffSize_Type(Unsigned32):defaultValue=1500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,9000))
_EltexIsisCircPDUBuffSize_Type.__name__=_E
_EltexIsisCircPDUBuffSize_Object=MibTableColumn
eltexIsisCircPDUBuffSize=_EltexIsisCircPDUBuffSize_Object((1,3,6,1,4,1,35265,55,1,2,1,1,9),_EltexIsisCircPDUBuffSize_Type())
eltexIsisCircPDUBuffSize.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisCircPDUBuffSize.setStatus(_A)
_EltexIsisCircLevelTable_Object=MibTable
eltexIsisCircLevelTable=_EltexIsisCircLevelTable_Object((1,3,6,1,4,1,35265,55,1,2,2))
if mibBuilder.loadTexts:eltexIsisCircLevelTable.setStatus(_A)
_EltexIsisCircLevelEntry_Object=MibTableRow
eltexIsisCircLevelEntry=_EltexIsisCircLevelEntry_Object((1,3,6,1,4,1,35265,55,1,2,2,1))
eltexIsisCircLevelEntry.setIndexNames((0,_B,_G),(0,_B,_J),(0,_B,_R))
if mibBuilder.loadTexts:eltexIsisCircLevelEntry.setStatus(_A)
class _EltexIsisCircLevelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_EltexIsisCircLevelIndex_Type.__name__=_F
_EltexIsisCircLevelIndex_Object=MibTableColumn
eltexIsisCircLevelIndex=_EltexIsisCircLevelIndex_Object((1,3,6,1,4,1,35265,55,1,2,2,1,1),_EltexIsisCircLevelIndex_Type())
eltexIsisCircLevelIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexIsisCircLevelIndex.setStatus(_A)
_EltexIsisCircLevelRowStatus_Type=RowStatus
_EltexIsisCircLevelRowStatus_Object=MibTableColumn
eltexIsisCircLevelRowStatus=_EltexIsisCircLevelRowStatus_Object((1,3,6,1,4,1,35265,55,1,2,2,1,2),_EltexIsisCircLevelRowStatus_Type())
eltexIsisCircLevelRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexIsisCircLevelRowStatus.setStatus(_A)
class _EltexIsisCircLevelMetric_Type(EltexIsisWideMetric):defaultValue=10
_EltexIsisCircLevelMetric_Type.__name__=_c
_EltexIsisCircLevelMetric_Object=MibTableColumn
eltexIsisCircLevelMetric=_EltexIsisCircLevelMetric_Object((1,3,6,1,4,1,35265,55,1,2,2,1,3),_EltexIsisCircLevelMetric_Type())
eltexIsisCircLevelMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisCircLevelMetric.setStatus(_A)
_EltexIsisCircLevelAuthType_Type=EltexIsisAuthType
_EltexIsisCircLevelAuthType_Object=MibTableColumn
eltexIsisCircLevelAuthType=_EltexIsisCircLevelAuthType_Object((1,3,6,1,4,1,35265,55,1,2,2,1,4),_EltexIsisCircLevelAuthType_Type())
eltexIsisCircLevelAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisCircLevelAuthType.setStatus(_A)
class _EltexIsisCircLevelAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_EltexIsisCircLevelAuthKey_Type.__name__=_K
_EltexIsisCircLevelAuthKey_Object=MibTableColumn
eltexIsisCircLevelAuthKey=_EltexIsisCircLevelAuthKey_Object((1,3,6,1,4,1,35265,55,1,2,2,1,5),_EltexIsisCircLevelAuthKey_Type())
eltexIsisCircLevelAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisCircLevelAuthKey.setStatus(_A)
class _EltexIsisCircLevelAuthKeyChain_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EltexIsisCircLevelAuthKeyChain_Type.__name__=_K
_EltexIsisCircLevelAuthKeyChain_Object=MibTableColumn
eltexIsisCircLevelAuthKeyChain=_EltexIsisCircLevelAuthKeyChain_Object((1,3,6,1,4,1,35265,55,1,2,2,1,6),_EltexIsisCircLevelAuthKeyChain_Type())
eltexIsisCircLevelAuthKeyChain.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIsisCircLevelAuthKeyChain.setStatus(_A)
_EltexIsisCircLevelStatusTable_Object=MibTable
eltexIsisCircLevelStatusTable=_EltexIsisCircLevelStatusTable_Object((1,3,6,1,4,1,35265,55,1,2,4))
if mibBuilder.loadTexts:eltexIsisCircLevelStatusTable.setStatus(_A)
_EltexIsisCircLevelStatusEntry_Object=MibTableRow
eltexIsisCircLevelStatusEntry=_EltexIsisCircLevelStatusEntry_Object((1,3,6,1,4,1,35265,55,1,2,4,1))
eltexIsisCircLevelStatusEntry.setIndexNames((0,_B,_G),(0,_B,_J),(0,_B,_R))
if mibBuilder.loadTexts:eltexIsisCircLevelStatusEntry.setStatus(_A)
_EltexIsisCircLevelStatusMetric_Type=Unsigned32
_EltexIsisCircLevelStatusMetric_Object=MibTableColumn
eltexIsisCircLevelStatusMetric=_EltexIsisCircLevelStatusMetric_Object((1,3,6,1,4,1,35265,55,1,2,4,1,1),_EltexIsisCircLevelStatusMetric_Type())
eltexIsisCircLevelStatusMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisCircLevelStatusMetric.setStatus(_A)
_EltexIsisISAdj_ObjectIdentity=ObjectIdentity
eltexIsisISAdj=_EltexIsisISAdj_ObjectIdentity((1,3,6,1,4,1,35265,55,1,3))
_EltexIsisISAdjTable_Object=MibTable
eltexIsisISAdjTable=_EltexIsisISAdjTable_Object((1,3,6,1,4,1,35265,55,1,3,1))
if mibBuilder.loadTexts:eltexIsisISAdjTable.setStatus(_A)
_EltexIsisISAdjEntry_Object=MibTableRow
eltexIsisISAdjEntry=_EltexIsisISAdjEntry_Object((1,3,6,1,4,1,35265,55,1,3,1,1))
eltexIsisISAdjEntry.setIndexNames((0,_B,_G),(0,_B,_J),(0,_B,_M))
if mibBuilder.loadTexts:eltexIsisISAdjEntry.setStatus(_A)
class _EltexIsisISAdjIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000000000))
_EltexIsisISAdjIndex_Type.__name__=_F
_EltexIsisISAdjIndex_Object=MibTableColumn
eltexIsisISAdjIndex=_EltexIsisISAdjIndex_Object((1,3,6,1,4,1,35265,55,1,3,1,1,1),_EltexIsisISAdjIndex_Type())
eltexIsisISAdjIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexIsisISAdjIndex.setStatus(_A)
class _EltexIsisISAdjState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('down',1),(_d,2),('up',3),(_e,4)))
_EltexIsisISAdjState_Type.__name__=_F
_EltexIsisISAdjState_Object=MibTableColumn
eltexIsisISAdjState=_EltexIsisISAdjState_Object((1,3,6,1,4,1,35265,55,1,3,1,1,2),_EltexIsisISAdjState_Type())
eltexIsisISAdjState.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjState.setStatus(_A)
class _EltexIsisISAdj3WayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('up',0),(_d,1),('down',2),(_e,3)))
_EltexIsisISAdj3WayState_Type.__name__=_F
_EltexIsisISAdj3WayState_Object=MibTableColumn
eltexIsisISAdj3WayState=_EltexIsisISAdj3WayState_Object((1,3,6,1,4,1,35265,55,1,3,1,1,3),_EltexIsisISAdj3WayState_Type())
eltexIsisISAdj3WayState.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdj3WayState.setStatus(_A)
_EltexIsisISAdjNeighSNPAAddress_Type=EltexNETAddress
_EltexIsisISAdjNeighSNPAAddress_Object=MibTableColumn
eltexIsisISAdjNeighSNPAAddress=_EltexIsisISAdjNeighSNPAAddress_Object((1,3,6,1,4,1,35265,55,1,3,1,1,4),_EltexIsisISAdjNeighSNPAAddress_Type())
eltexIsisISAdjNeighSNPAAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjNeighSNPAAddress.setStatus(_A)
class _EltexIsisISAdjNeighSysType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('l1IntermediateSystem',1),('l2IntermediateSystem',2),('l1L2IntermediateSystem',3),('unknown',4)))
_EltexIsisISAdjNeighSysType_Type.__name__=_F
_EltexIsisISAdjNeighSysType_Object=MibTableColumn
eltexIsisISAdjNeighSysType=_EltexIsisISAdjNeighSysType_Object((1,3,6,1,4,1,35265,55,1,3,1,1,5),_EltexIsisISAdjNeighSysType_Type())
eltexIsisISAdjNeighSysType.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjNeighSysType.setStatus(_A)
_EltexIsisISAdjNeighSysID_Type=EltexIsisSystemID
_EltexIsisISAdjNeighSysID_Object=MibTableColumn
eltexIsisISAdjNeighSysID=_EltexIsisISAdjNeighSysID_Object((1,3,6,1,4,1,35265,55,1,3,1,1,6),_EltexIsisISAdjNeighSysID_Type())
eltexIsisISAdjNeighSysID.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjNeighSysID.setStatus(_A)
_EltexIsisISAdjNbrExtendedCircID_Type=Unsigned32
_EltexIsisISAdjNbrExtendedCircID_Object=MibTableColumn
eltexIsisISAdjNbrExtendedCircID=_EltexIsisISAdjNbrExtendedCircID_Object((1,3,6,1,4,1,35265,55,1,3,1,1,7),_EltexIsisISAdjNbrExtendedCircID_Type())
eltexIsisISAdjNbrExtendedCircID.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjNbrExtendedCircID.setStatus(_A)
class _EltexIsisISAdjUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),(_Z,1),(_a,2),('level1and2',3)))
_EltexIsisISAdjUsage_Type.__name__=_F
_EltexIsisISAdjUsage_Object=MibTableColumn
eltexIsisISAdjUsage=_EltexIsisISAdjUsage_Object((1,3,6,1,4,1,35265,55,1,3,1,1,8),_EltexIsisISAdjUsage_Type())
eltexIsisISAdjUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjUsage.setStatus(_A)
class _EltexIsisISAdjHoldTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EltexIsisISAdjHoldTimer_Type.__name__=_E
_EltexIsisISAdjHoldTimer_Object=MibTableColumn
eltexIsisISAdjHoldTimer=_EltexIsisISAdjHoldTimer_Object((1,3,6,1,4,1,35265,55,1,3,1,1,9),_EltexIsisISAdjHoldTimer_Type())
eltexIsisISAdjHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjHoldTimer.setStatus(_A)
if mibBuilder.loadTexts:eltexIsisISAdjHoldTimer.setUnits(_S)
_EltexIsisISAdjNeighPriority_Type=EltexIsisISPriority
_EltexIsisISAdjNeighPriority_Object=MibTableColumn
eltexIsisISAdjNeighPriority=_EltexIsisISAdjNeighPriority_Object((1,3,6,1,4,1,35265,55,1,3,1,1,10),_EltexIsisISAdjNeighPriority_Type())
eltexIsisISAdjNeighPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjNeighPriority.setStatus(_A)
_EltexIsisISAdjLastUpTime_Type=TimeTicks
_EltexIsisISAdjLastUpTime_Object=MibTableColumn
eltexIsisISAdjLastUpTime=_EltexIsisISAdjLastUpTime_Object((1,3,6,1,4,1,35265,55,1,3,1,1,11),_EltexIsisISAdjLastUpTime_Type())
eltexIsisISAdjLastUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjLastUpTime.setStatus(_A)
if mibBuilder.loadTexts:eltexIsisISAdjLastUpTime.setUnits(_S)
_EltexIsisISAdjRestartCapable_Type=TruthValue
_EltexIsisISAdjRestartCapable_Object=MibTableColumn
eltexIsisISAdjRestartCapable=_EltexIsisISAdjRestartCapable_Object((1,3,6,1,4,1,35265,55,1,3,1,1,12),_EltexIsisISAdjRestartCapable_Type())
eltexIsisISAdjRestartCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjRestartCapable.setStatus(_A)
class _EltexIsisISAdjPeerRestartState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notRestarting',1),('restartingNoHelp',2),('helpingRestart',3)))
_EltexIsisISAdjPeerRestartState_Type.__name__=_F
_EltexIsisISAdjPeerRestartState_Object=MibTableColumn
eltexIsisISAdjPeerRestartState=_EltexIsisISAdjPeerRestartState_Object((1,3,6,1,4,1,35265,55,1,3,1,1,13),_EltexIsisISAdjPeerRestartState_Type())
eltexIsisISAdjPeerRestartState.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjPeerRestartState.setStatus(_A)
_EltexIsisISAdjSuppressed_Type=TruthValue
_EltexIsisISAdjSuppressed_Object=MibTableColumn
eltexIsisISAdjSuppressed=_EltexIsisISAdjSuppressed_Object((1,3,6,1,4,1,35265,55,1,3,1,1,14),_EltexIsisISAdjSuppressed_Type())
eltexIsisISAdjSuppressed.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjSuppressed.setStatus(_A)
class _EltexIsisISAdjNeighLanID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_EltexIsisISAdjNeighLanID_Type.__name__=_K
_EltexIsisISAdjNeighLanID_Object=MibTableColumn
eltexIsisISAdjNeighLanID=_EltexIsisISAdjNeighLanID_Object((1,3,6,1,4,1,35265,55,1,3,1,1,15),_EltexIsisISAdjNeighLanID_Type())
eltexIsisISAdjNeighLanID.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjNeighLanID.setStatus(_A)
_EltexIsisISAdjNeighHostname_Type=SnmpAdminString
_EltexIsisISAdjNeighHostname_Object=MibTableColumn
eltexIsisISAdjNeighHostname=_EltexIsisISAdjNeighHostname_Object((1,3,6,1,4,1,35265,55,1,3,1,1,16),_EltexIsisISAdjNeighHostname_Type())
eltexIsisISAdjNeighHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjNeighHostname.setStatus(_A)
_EltexIsisISAdjNeighLanIDHostname_Type=SnmpAdminString
_EltexIsisISAdjNeighLanIDHostname_Object=MibTableColumn
eltexIsisISAdjNeighLanIDHostname=_EltexIsisISAdjNeighLanIDHostname_Object((1,3,6,1,4,1,35265,55,1,3,1,1,17),_EltexIsisISAdjNeighLanIDHostname_Type())
eltexIsisISAdjNeighLanIDHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjNeighLanIDHostname.setStatus(_A)
_EltexIsisISAdjAreaAddrTable_Object=MibTable
eltexIsisISAdjAreaAddrTable=_EltexIsisISAdjAreaAddrTable_Object((1,3,6,1,4,1,35265,55,1,3,2))
if mibBuilder.loadTexts:eltexIsisISAdjAreaAddrTable.setStatus(_A)
_EltexIsisISAdjAreaAddrEntry_Object=MibTableRow
eltexIsisISAdjAreaAddrEntry=_EltexIsisISAdjAreaAddrEntry_Object((1,3,6,1,4,1,35265,55,1,3,2,1))
eltexIsisISAdjAreaAddrEntry.setIndexNames((0,_B,_G),(0,_B,_J),(0,_B,_M),(0,_B,_f))
if mibBuilder.loadTexts:eltexIsisISAdjAreaAddrEntry.setStatus(_A)
class _EltexIsisISAdjAreaAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000000000))
_EltexIsisISAdjAreaAddrIndex_Type.__name__=_F
_EltexIsisISAdjAreaAddrIndex_Object=MibTableColumn
eltexIsisISAdjAreaAddrIndex=_EltexIsisISAdjAreaAddrIndex_Object((1,3,6,1,4,1,35265,55,1,3,2,1,1),_EltexIsisISAdjAreaAddrIndex_Type())
eltexIsisISAdjAreaAddrIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexIsisISAdjAreaAddrIndex.setStatus(_A)
_EltexIsisISAdjAreaAddress_Type=EltexNETAddress
_EltexIsisISAdjAreaAddress_Object=MibTableColumn
eltexIsisISAdjAreaAddress=_EltexIsisISAdjAreaAddress_Object((1,3,6,1,4,1,35265,55,1,3,2,1,2),_EltexIsisISAdjAreaAddress_Type())
eltexIsisISAdjAreaAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjAreaAddress.setStatus(_A)
_EltexIsisISAdjIPAddrTable_Object=MibTable
eltexIsisISAdjIPAddrTable=_EltexIsisISAdjIPAddrTable_Object((1,3,6,1,4,1,35265,55,1,3,3))
if mibBuilder.loadTexts:eltexIsisISAdjIPAddrTable.setStatus(_A)
_EltexIsisISAdjIPAddrEntry_Object=MibTableRow
eltexIsisISAdjIPAddrEntry=_EltexIsisISAdjIPAddrEntry_Object((1,3,6,1,4,1,35265,55,1,3,3,1))
eltexIsisISAdjIPAddrEntry.setIndexNames((0,_B,_G),(0,_B,_J),(0,_B,_M),(0,_B,_g))
if mibBuilder.loadTexts:eltexIsisISAdjIPAddrEntry.setStatus(_A)
class _EltexIsisISAdjIPAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000000000))
_EltexIsisISAdjIPAddrIndex_Type.__name__=_F
_EltexIsisISAdjIPAddrIndex_Object=MibTableColumn
eltexIsisISAdjIPAddrIndex=_EltexIsisISAdjIPAddrIndex_Object((1,3,6,1,4,1,35265,55,1,3,3,1,1),_EltexIsisISAdjIPAddrIndex_Type())
eltexIsisISAdjIPAddrIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexIsisISAdjIPAddrIndex.setStatus(_A)
_EltexIsisISAdjIPAddrType_Type=InetAddressType
_EltexIsisISAdjIPAddrType_Object=MibTableColumn
eltexIsisISAdjIPAddrType=_EltexIsisISAdjIPAddrType_Object((1,3,6,1,4,1,35265,55,1,3,3,1,2),_EltexIsisISAdjIPAddrType_Type())
eltexIsisISAdjIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjIPAddrType.setStatus(_A)
class _EltexIsisISAdjIPAddrAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_EltexIsisISAdjIPAddrAddress_Type.__name__=_T
_EltexIsisISAdjIPAddrAddress_Object=MibTableColumn
eltexIsisISAdjIPAddrAddress=_EltexIsisISAdjIPAddrAddress_Object((1,3,6,1,4,1,35265,55,1,3,3,1,3),_EltexIsisISAdjIPAddrAddress_Type())
eltexIsisISAdjIPAddrAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisISAdjIPAddrAddress.setStatus(_A)
_EltexIsisLSPDataBase_ObjectIdentity=ObjectIdentity
eltexIsisLSPDataBase=_EltexIsisLSPDataBase_ObjectIdentity((1,3,6,1,4,1,35265,55,1,5))
_EltexIsisLSPSummaryTable_Object=MibTable
eltexIsisLSPSummaryTable=_EltexIsisLSPSummaryTable_Object((1,3,6,1,4,1,35265,55,1,5,1))
if mibBuilder.loadTexts:eltexIsisLSPSummaryTable.setStatus(_A)
_EltexIsisLSPSummaryEntry_Object=MibTableRow
eltexIsisLSPSummaryEntry=_EltexIsisLSPSummaryEntry_Object((1,3,6,1,4,1,35265,55,1,5,1,1))
eltexIsisLSPSummaryEntry.setIndexNames((0,_B,_G),(0,_B,_h),(0,_B,_i))
if mibBuilder.loadTexts:eltexIsisLSPSummaryEntry.setStatus(_A)
_EltexIsisLSPLevel_Type=EltexIsisISLevel
_EltexIsisLSPLevel_Object=MibTableColumn
eltexIsisLSPLevel=_EltexIsisLSPLevel_Object((1,3,6,1,4,1,35265,55,1,5,1,1,1),_EltexIsisLSPLevel_Type())
eltexIsisLSPLevel.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexIsisLSPLevel.setStatus(_A)
_EltexIsisLSPID_Type=EltexIsisLinkStatePDUID
_EltexIsisLSPID_Object=MibTableColumn
eltexIsisLSPID=_EltexIsisLSPID_Object((1,3,6,1,4,1,35265,55,1,5,1,1,2),_EltexIsisLSPID_Type())
eltexIsisLSPID.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexIsisLSPID.setStatus(_A)
_EltexIsisLSPSeq_Type=Unsigned32
_EltexIsisLSPSeq_Object=MibTableColumn
eltexIsisLSPSeq=_EltexIsisLSPSeq_Object((1,3,6,1,4,1,35265,55,1,5,1,1,3),_EltexIsisLSPSeq_Type())
eltexIsisLSPSeq.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisLSPSeq.setStatus(_A)
_EltexIsisLSPZeroLife_Type=TruthValue
_EltexIsisLSPZeroLife_Object=MibTableColumn
eltexIsisLSPZeroLife=_EltexIsisLSPZeroLife_Object((1,3,6,1,4,1,35265,55,1,5,1,1,4),_EltexIsisLSPZeroLife_Type())
eltexIsisLSPZeroLife.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisLSPZeroLife.setStatus(_A)
class _EltexIsisLSPChecksum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexIsisLSPChecksum_Type.__name__=_E
_EltexIsisLSPChecksum_Object=MibTableColumn
eltexIsisLSPChecksum=_EltexIsisLSPChecksum_Object((1,3,6,1,4,1,35265,55,1,5,1,1,5),_EltexIsisLSPChecksum_Type())
eltexIsisLSPChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisLSPChecksum.setStatus(_A)
class _EltexIsisLSPLifetimeRemain_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexIsisLSPLifetimeRemain_Type.__name__=_E
_EltexIsisLSPLifetimeRemain_Object=MibTableColumn
eltexIsisLSPLifetimeRemain=_EltexIsisLSPLifetimeRemain_Object((1,3,6,1,4,1,35265,55,1,5,1,1,6),_EltexIsisLSPLifetimeRemain_Type())
eltexIsisLSPLifetimeRemain.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisLSPLifetimeRemain.setStatus(_A)
if mibBuilder.loadTexts:eltexIsisLSPLifetimeRemain.setUnits(_S)
class _EltexIsisLSPPDULength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexIsisLSPPDULength_Type.__name__=_E
_EltexIsisLSPPDULength_Object=MibTableColumn
eltexIsisLSPPDULength=_EltexIsisLSPPDULength_Object((1,3,6,1,4,1,35265,55,1,5,1,1,7),_EltexIsisLSPPDULength_Type())
eltexIsisLSPPDULength.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisLSPPDULength.setStatus(_A)
class _EltexIsisLSPAttributes_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EltexIsisLSPAttributes_Type.__name__=_E
_EltexIsisLSPAttributes_Object=MibTableColumn
eltexIsisLSPAttributes=_EltexIsisLSPAttributes_Object((1,3,6,1,4,1,35265,55,1,5,1,1,8),_EltexIsisLSPAttributes_Type())
eltexIsisLSPAttributes.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisLSPAttributes.setStatus(_A)
_EltexIsisLSPIDHostname_Type=SnmpAdminString
_EltexIsisLSPIDHostname_Object=MibTableColumn
eltexIsisLSPIDHostname=_EltexIsisLSPIDHostname_Object((1,3,6,1,4,1,35265,55,1,5,1,1,9),_EltexIsisLSPIDHostname_Type())
eltexIsisLSPIDHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexIsisLSPIDHostname.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EltexIsisSystemID':EltexIsisSystemID,_Q:EltexIsisAdminState,'EltexNETAddress':EltexNETAddress,'EltexIsisOperStatus':EltexIsisOperStatus,'EltexIsisISLevel':EltexIsisISLevel,'EltexIsisLinkStatePDUID':EltexIsisLinkStatePDUID,'EltexIsisISPriority':EltexIsisISPriority,_W:EltexIsisMetricStyle,_c:EltexIsisWideMetric,'EltexIsisAuthType':EltexIsisAuthType,_b:EltexIsisHelloPaddingAction,'eltexIsisMIB':eltexIsisMIB,'eltexIsisObjects':eltexIsisObjects,'eltexIsisSystem':eltexIsisSystem,'eltexIsisSysTable':eltexIsisSysTable,'eltexIsisSysEntry':eltexIsisSysEntry,_G:eltexIsisSysInstance,'eltexIsisSysType':eltexIsisSysType,'eltexIsisSysID':eltexIsisSysID,'eltexIsisSysAdminState':eltexIsisSysAdminState,'eltexIsisSysOperState':eltexIsisSysOperState,'eltexIsisSysRowStatus':eltexIsisSysRowStatus,'eltexIsisSysMaxAge':eltexIsisSysMaxAge,'eltexIsisSysMaxLSPGenInt':eltexIsisSysMaxLSPGenInt,'eltexIsisSysCalcMaxDelay':eltexIsisSysCalcMaxDelay,'eltexIsisSysCalcThrshUpdStart':eltexIsisSysCalcThrshUpdStart,'eltexIsisSysCalcThrshUpdRestart':eltexIsisSysCalcThrshUpdRestart,'eltexIsisSysCalcThrshRestartLimit':eltexIsisSysCalcThrshRestartLimit,'eltexIsisSysHostNameDynamic':eltexIsisSysHostNameDynamic,'eltexIsisNetAddrTable':eltexIsisNetAddrTable,'eltexIsisNetAddrEntry':eltexIsisNetAddrEntry,_U:eltexIsisNetAddr,'eltexIsisNetAddrRowStatus':eltexIsisNetAddrRowStatus,'eltexIsisSysLevelTable':eltexIsisSysLevelTable,'eltexIsisSysLevelEntry':eltexIsisSysLevelEntry,_V:eltexIsisSysLevelIndex,'eltexIsisSysLevelMinLSPGenInt':eltexIsisSysLevelMinLSPGenInt,'eltexIsisSysLevelMetricStyle':eltexIsisSysLevelMetricStyle,'eltexIsisSysLevelAuthType':eltexIsisSysLevelAuthType,'eltexIsisSysLevelAuthKey':eltexIsisSysLevelAuthKey,'eltexIsisSysLevelAuthKeyChain':eltexIsisSysLevelAuthKeyChain,'eltexIsisSysLevelOrigLSPBuffSize':eltexIsisSysLevelOrigLSPBuffSize,'eltexIsisRouterTable':eltexIsisRouterTable,'eltexIsisRouterEntry':eltexIsisRouterEntry,_X:eltexIsisRouterSysID,_Y:eltexIsisRouterLevel,'eltexIsisRouterHostName':eltexIsisRouterHostName,'eltexIsisCirc':eltexIsisCirc,'eltexIsisCircTable':eltexIsisCircTable,'eltexIsisCircEntry':eltexIsisCircEntry,_J:eltexIsisCircIfindex,'eltexIsisCircRowStatus':eltexIsisCircRowStatus,'eltexIsisCircAdminState':eltexIsisCircAdminState,'eltexIsisCircOperState':eltexIsisCircOperState,'eltexIsisCircLevel':eltexIsisCircLevel,'eltexIsisCircPassiveCircuit':eltexIsisCircPassiveCircuit,'eltexIsisCircPtToPt':eltexIsisCircPtToPt,'eltexIsisCircHelloPadding':eltexIsisCircHelloPadding,'eltexIsisCircPDUBuffSize':eltexIsisCircPDUBuffSize,'eltexIsisCircLevelTable':eltexIsisCircLevelTable,'eltexIsisCircLevelEntry':eltexIsisCircLevelEntry,_R:eltexIsisCircLevelIndex,'eltexIsisCircLevelRowStatus':eltexIsisCircLevelRowStatus,'eltexIsisCircLevelMetric':eltexIsisCircLevelMetric,'eltexIsisCircLevelAuthType':eltexIsisCircLevelAuthType,'eltexIsisCircLevelAuthKey':eltexIsisCircLevelAuthKey,'eltexIsisCircLevelAuthKeyChain':eltexIsisCircLevelAuthKeyChain,'eltexIsisCircLevelStatusTable':eltexIsisCircLevelStatusTable,'eltexIsisCircLevelStatusEntry':eltexIsisCircLevelStatusEntry,'eltexIsisCircLevelStatusMetric':eltexIsisCircLevelStatusMetric,'eltexIsisISAdj':eltexIsisISAdj,'eltexIsisISAdjTable':eltexIsisISAdjTable,'eltexIsisISAdjEntry':eltexIsisISAdjEntry,_M:eltexIsisISAdjIndex,'eltexIsisISAdjState':eltexIsisISAdjState,'eltexIsisISAdj3WayState':eltexIsisISAdj3WayState,'eltexIsisISAdjNeighSNPAAddress':eltexIsisISAdjNeighSNPAAddress,'eltexIsisISAdjNeighSysType':eltexIsisISAdjNeighSysType,'eltexIsisISAdjNeighSysID':eltexIsisISAdjNeighSysID,'eltexIsisISAdjNbrExtendedCircID':eltexIsisISAdjNbrExtendedCircID,'eltexIsisISAdjUsage':eltexIsisISAdjUsage,'eltexIsisISAdjHoldTimer':eltexIsisISAdjHoldTimer,'eltexIsisISAdjNeighPriority':eltexIsisISAdjNeighPriority,'eltexIsisISAdjLastUpTime':eltexIsisISAdjLastUpTime,'eltexIsisISAdjRestartCapable':eltexIsisISAdjRestartCapable,'eltexIsisISAdjPeerRestartState':eltexIsisISAdjPeerRestartState,'eltexIsisISAdjSuppressed':eltexIsisISAdjSuppressed,'eltexIsisISAdjNeighLanID':eltexIsisISAdjNeighLanID,'eltexIsisISAdjNeighHostname':eltexIsisISAdjNeighHostname,'eltexIsisISAdjNeighLanIDHostname':eltexIsisISAdjNeighLanIDHostname,'eltexIsisISAdjAreaAddrTable':eltexIsisISAdjAreaAddrTable,'eltexIsisISAdjAreaAddrEntry':eltexIsisISAdjAreaAddrEntry,_f:eltexIsisISAdjAreaAddrIndex,'eltexIsisISAdjAreaAddress':eltexIsisISAdjAreaAddress,'eltexIsisISAdjIPAddrTable':eltexIsisISAdjIPAddrTable,'eltexIsisISAdjIPAddrEntry':eltexIsisISAdjIPAddrEntry,_g:eltexIsisISAdjIPAddrIndex,'eltexIsisISAdjIPAddrType':eltexIsisISAdjIPAddrType,'eltexIsisISAdjIPAddrAddress':eltexIsisISAdjIPAddrAddress,'eltexIsisLSPDataBase':eltexIsisLSPDataBase,'eltexIsisLSPSummaryTable':eltexIsisLSPSummaryTable,'eltexIsisLSPSummaryEntry':eltexIsisLSPSummaryEntry,_h:eltexIsisLSPLevel,_i:eltexIsisLSPID,'eltexIsisLSPSeq':eltexIsisLSPSeq,'eltexIsisLSPZeroLife':eltexIsisLSPZeroLife,'eltexIsisLSPChecksum':eltexIsisLSPChecksum,'eltexIsisLSPLifetimeRemain':eltexIsisLSPLifetimeRemain,'eltexIsisLSPPDULength':eltexIsisLSPPDULength,'eltexIsisLSPAttributes':eltexIsisLSPAttributes,'eltexIsisLSPIDHostname':eltexIsisLSPIDHostname})