_G='extremeTargetAddrExtEntry'
_F='EXTREME-SNMPV3-MIB'
_E='read-create'
_D='DisplayString'
_C='TruthValue'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
snmpTargetAddrEntry,=mibBuilder.importSymbols('SNMP-TARGET-MIB','snmpTargetAddrEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention',_C)
extremeSnmpv3=ModuleIdentity((1,3,6,1,4,1,1916,1,23))
_ExtremeTarget_ObjectIdentity=ObjectIdentity
extremeTarget=_ExtremeTarget_ObjectIdentity((1,3,6,1,4,1,1916,1,23,1))
_ExtremeTargetAddrExtTable_Object=MibTable
extremeTargetAddrExtTable=_ExtremeTargetAddrExtTable_Object((1,3,6,1,4,1,1916,1,23,1,1))
if mibBuilder.loadTexts:extremeTargetAddrExtTable.setStatus(_A)
_ExtremeTargetAddrExtEntry_Object=MibTableRow
extremeTargetAddrExtEntry=_ExtremeTargetAddrExtEntry_Object((1,3,6,1,4,1,1916,1,23,1,1,1))
if mibBuilder.loadTexts:extremeTargetAddrExtEntry.setStatus(_A)
class _ExtremeTargetAddrExtIgnoreMPModel_Type(TruthValue):defaultValue=2
_ExtremeTargetAddrExtIgnoreMPModel_Type.__name__=_C
_ExtremeTargetAddrExtIgnoreMPModel_Object=MibTableColumn
extremeTargetAddrExtIgnoreMPModel=_ExtremeTargetAddrExtIgnoreMPModel_Object((1,3,6,1,4,1,1916,1,23,1,1,1,1),_ExtremeTargetAddrExtIgnoreMPModel_Type())
extremeTargetAddrExtIgnoreMPModel.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTargetAddrExtIgnoreMPModel.setStatus(_A)
class _ExtremeTargetAddrExtStandardMode_Type(TruthValue):defaultValue=2
_ExtremeTargetAddrExtStandardMode_Type.__name__=_C
_ExtremeTargetAddrExtStandardMode_Object=MibTableColumn
extremeTargetAddrExtStandardMode=_ExtremeTargetAddrExtStandardMode_Object((1,3,6,1,4,1,1916,1,23,1,1,1,2),_ExtremeTargetAddrExtStandardMode_Type())
extremeTargetAddrExtStandardMode.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTargetAddrExtStandardMode.setStatus(_A)
_ExtremeTargetAddrExtTrapDestIndex_Type=Integer32
_ExtremeTargetAddrExtTrapDestIndex_Object=MibTableColumn
extremeTargetAddrExtTrapDestIndex=_ExtremeTargetAddrExtTrapDestIndex_Object((1,3,6,1,4,1,1916,1,23,1,1,1,3),_ExtremeTargetAddrExtTrapDestIndex_Type())
extremeTargetAddrExtTrapDestIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:extremeTargetAddrExtTrapDestIndex.setStatus(_A)
class _ExtremeTargetAddrExtUseEventComm_Type(TruthValue):defaultValue=1
_ExtremeTargetAddrExtUseEventComm_Type.__name__=_C
_ExtremeTargetAddrExtUseEventComm_Object=MibTableColumn
extremeTargetAddrExtUseEventComm=_ExtremeTargetAddrExtUseEventComm_Object((1,3,6,1,4,1,1916,1,23,1,1,1,4),_ExtremeTargetAddrExtUseEventComm_Type())
extremeTargetAddrExtUseEventComm.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTargetAddrExtUseEventComm.setStatus(_A)
_ExtremeTargetAddrExtTrapSrcIp_Type=IpAddress
_ExtremeTargetAddrExtTrapSrcIp_Object=MibTableColumn
extremeTargetAddrExtTrapSrcIp=_ExtremeTargetAddrExtTrapSrcIp_Object((1,3,6,1,4,1,1916,1,23,1,1,1,5),_ExtremeTargetAddrExtTrapSrcIp_Type())
extremeTargetAddrExtTrapSrcIp.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTargetAddrExtTrapSrcIp.setStatus('deprecated')
class _ExtremeTargetAddrExtVrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeTargetAddrExtVrName_Type.__name__=_D
_ExtremeTargetAddrExtVrName_Object=MibTableColumn
extremeTargetAddrExtVrName=_ExtremeTargetAddrExtVrName_Object((1,3,6,1,4,1,1916,1,23,1,1,1,6),_ExtremeTargetAddrExtVrName_Type())
extremeTargetAddrExtVrName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTargetAddrExtVrName.setStatus(_A)
_ExtremeTargetAddrExtTrapSrcAddrType_Type=InetAddressType
_ExtremeTargetAddrExtTrapSrcAddrType_Object=MibTableColumn
extremeTargetAddrExtTrapSrcAddrType=_ExtremeTargetAddrExtTrapSrcAddrType_Object((1,3,6,1,4,1,1916,1,23,1,1,1,7),_ExtremeTargetAddrExtTrapSrcAddrType_Type())
extremeTargetAddrExtTrapSrcAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeTargetAddrExtTrapSrcAddrType.setStatus(_A)
_ExtremeTargetAddrExtTrapSrcAddr_Type=InetAddress
_ExtremeTargetAddrExtTrapSrcAddr_Object=MibTableColumn
extremeTargetAddrExtTrapSrcAddr=_ExtremeTargetAddrExtTrapSrcAddr_Object((1,3,6,1,4,1,1916,1,23,1,1,1,8),_ExtremeTargetAddrExtTrapSrcAddr_Type())
extremeTargetAddrExtTrapSrcAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeTargetAddrExtTrapSrcAddr.setStatus(_A)
_ExtremeUsm_ObjectIdentity=ObjectIdentity
extremeUsm=_ExtremeUsm_ObjectIdentity((1,3,6,1,4,1,1916,1,23,2))
_ExtremeUsm3DESPrivProtocol_ObjectIdentity=ObjectIdentity
extremeUsm3DESPrivProtocol=_ExtremeUsm3DESPrivProtocol_ObjectIdentity((1,3,6,1,4,1,1916,1,23,2,1))
if mibBuilder.loadTexts:extremeUsm3DESPrivProtocol.setStatus(_A)
_ExtremeUsmAesCfb192Protocol_ObjectIdentity=ObjectIdentity
extremeUsmAesCfb192Protocol=_ExtremeUsmAesCfb192Protocol_ObjectIdentity((1,3,6,1,4,1,1916,1,23,2,2))
if mibBuilder.loadTexts:extremeUsmAesCfb192Protocol.setStatus(_A)
_ExtremeUsmAesCfb256Protocol_ObjectIdentity=ObjectIdentity
extremeUsmAesCfb256Protocol=_ExtremeUsmAesCfb256Protocol_ObjectIdentity((1,3,6,1,4,1,1916,1,23,2,3))
if mibBuilder.loadTexts:extremeUsmAesCfb256Protocol.setStatus(_A)
snmpTargetAddrEntry.registerAugmentions((_F,_G))
extremeTargetAddrExtEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'extremeSnmpv3':extremeSnmpv3,'extremeTarget':extremeTarget,'extremeTargetAddrExtTable':extremeTargetAddrExtTable,_G:extremeTargetAddrExtEntry,'extremeTargetAddrExtIgnoreMPModel':extremeTargetAddrExtIgnoreMPModel,'extremeTargetAddrExtStandardMode':extremeTargetAddrExtStandardMode,'extremeTargetAddrExtTrapDestIndex':extremeTargetAddrExtTrapDestIndex,'extremeTargetAddrExtUseEventComm':extremeTargetAddrExtUseEventComm,'extremeTargetAddrExtTrapSrcIp':extremeTargetAddrExtTrapSrcIp,'extremeTargetAddrExtVrName':extremeTargetAddrExtVrName,'extremeTargetAddrExtTrapSrcAddrType':extremeTargetAddrExtTrapSrcAddrType,'extremeTargetAddrExtTrapSrcAddr':extremeTargetAddrExtTrapSrcAddr,'extremeUsm':extremeUsm,'extremeUsm3DESPrivProtocol':extremeUsm3DESPrivProtocol,'extremeUsmAesCfb192Protocol':extremeUsmAesCfb192Protocol,'extremeUsmAesCfb256Protocol':extremeUsmAesCfb256Protocol})