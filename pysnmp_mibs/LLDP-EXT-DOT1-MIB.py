_o='lldpXdot1RemSysGroup'
_n='lldpXdot1LocSysGroup'
_m='lldpXdot1ConfigGroup'
_l='lldpXdot1RemProtocolId'
_k='lldpXdot1RemVlanName'
_j='lldpXdot1RemProtoVlanEnabled'
_i='lldpXdot1RemProtoVlanSupported'
_h='lldpXdot1RemPortVlanId'
_g='lldpXdot1LocProtocolId'
_f='lldpXdot1LocVlanName'
_e='lldpXdot1LocProtoVlanEnabled'
_d='lldpXdot1LocProtoVlanSupported'
_c='lldpXdot1LocPortVlanId'
_b='lldpXdot1ConfigProtocolTxEnable'
_a='lldpXdot1ConfigProtoVlanTxEnable'
_Z='lldpXdot1ConfigVlanNameTxEnable'
_Y='lldpXdot1ConfigPortVlanTxEnable'
_X='lldpXdot1ConfigProtocolEntry'
_W='lldpXdot1ConfigProtoVlanEntry'
_V='lldpXdot1ConfigVlanNameEntry'
_U='lldpXdot1ConfigPortVlanEntry'
_T='lldpXdot1RemProtocolIndex'
_S='lldpXdot1RemVlanId'
_R='lldpXdot1RemProtoVlanId'
_Q='lldpXdot1LocProtocolIndex'
_P='lldpXdot1LocVlanId'
_O='lldpXdot1LocProtoVlanId'
_N='SnmpAdminString'
_M='OctetString'
_L='read-write'
_K='TruthValue'
_J='lldpRemTimeMark'
_I='lldpRemLocalPortNum'
_H='lldpRemIndex'
_G='lldpLocPortNum'
_F='not-accessible'
_E='Integer32'
_D='read-only'
_C='LLDP-MIB'
_B='LLDP-EXT-DOT1-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lldpExtensions,lldpLocPortNum,lldpPortConfigEntry,lldpRemIndex,lldpRemLocalPortNum,lldpRemTimeMark=mibBuilder.importSymbols(_C,'lldpExtensions',_G,'lldpPortConfigEntry',_H,_I,_J)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_K)
lldpXdot1MIB=ModuleIdentity((1,0,8802,1,1,2,1,5,32962))
if mibBuilder.loadTexts:lldpXdot1MIB.setRevisions(('2005-05-06 00:00',))
_LldpXdot1Objects_ObjectIdentity=ObjectIdentity
lldpXdot1Objects=_LldpXdot1Objects_ObjectIdentity((1,0,8802,1,1,2,1,5,32962,1))
_LldpXdot1Config_ObjectIdentity=ObjectIdentity
lldpXdot1Config=_LldpXdot1Config_ObjectIdentity((1,0,8802,1,1,2,1,5,32962,1,1))
_LldpXdot1ConfigPortVlanTable_Object=MibTable
lldpXdot1ConfigPortVlanTable=_LldpXdot1ConfigPortVlanTable_Object((1,0,8802,1,1,2,1,5,32962,1,1,1))
if mibBuilder.loadTexts:lldpXdot1ConfigPortVlanTable.setStatus(_A)
_LldpXdot1ConfigPortVlanEntry_Object=MibTableRow
lldpXdot1ConfigPortVlanEntry=_LldpXdot1ConfigPortVlanEntry_Object((1,0,8802,1,1,2,1,5,32962,1,1,1,1))
if mibBuilder.loadTexts:lldpXdot1ConfigPortVlanEntry.setStatus(_A)
class _LldpXdot1ConfigPortVlanTxEnable_Type(TruthValue):defaultValue=2
_LldpXdot1ConfigPortVlanTxEnable_Type.__name__=_K
_LldpXdot1ConfigPortVlanTxEnable_Object=MibTableColumn
lldpXdot1ConfigPortVlanTxEnable=_LldpXdot1ConfigPortVlanTxEnable_Object((1,0,8802,1,1,2,1,5,32962,1,1,1,1,1),_LldpXdot1ConfigPortVlanTxEnable_Type())
lldpXdot1ConfigPortVlanTxEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:lldpXdot1ConfigPortVlanTxEnable.setStatus(_A)
_LldpXdot1ConfigVlanNameTable_Object=MibTable
lldpXdot1ConfigVlanNameTable=_LldpXdot1ConfigVlanNameTable_Object((1,0,8802,1,1,2,1,5,32962,1,1,2))
if mibBuilder.loadTexts:lldpXdot1ConfigVlanNameTable.setStatus(_A)
_LldpXdot1ConfigVlanNameEntry_Object=MibTableRow
lldpXdot1ConfigVlanNameEntry=_LldpXdot1ConfigVlanNameEntry_Object((1,0,8802,1,1,2,1,5,32962,1,1,2,1))
if mibBuilder.loadTexts:lldpXdot1ConfigVlanNameEntry.setStatus(_A)
class _LldpXdot1ConfigVlanNameTxEnable_Type(TruthValue):defaultValue=2
_LldpXdot1ConfigVlanNameTxEnable_Type.__name__=_K
_LldpXdot1ConfigVlanNameTxEnable_Object=MibTableColumn
lldpXdot1ConfigVlanNameTxEnable=_LldpXdot1ConfigVlanNameTxEnable_Object((1,0,8802,1,1,2,1,5,32962,1,1,2,1,1),_LldpXdot1ConfigVlanNameTxEnable_Type())
lldpXdot1ConfigVlanNameTxEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:lldpXdot1ConfigVlanNameTxEnable.setStatus(_A)
_LldpXdot1ConfigProtoVlanTable_Object=MibTable
lldpXdot1ConfigProtoVlanTable=_LldpXdot1ConfigProtoVlanTable_Object((1,0,8802,1,1,2,1,5,32962,1,1,3))
if mibBuilder.loadTexts:lldpXdot1ConfigProtoVlanTable.setStatus(_A)
_LldpXdot1ConfigProtoVlanEntry_Object=MibTableRow
lldpXdot1ConfigProtoVlanEntry=_LldpXdot1ConfigProtoVlanEntry_Object((1,0,8802,1,1,2,1,5,32962,1,1,3,1))
if mibBuilder.loadTexts:lldpXdot1ConfigProtoVlanEntry.setStatus(_A)
class _LldpXdot1ConfigProtoVlanTxEnable_Type(TruthValue):defaultValue=2
_LldpXdot1ConfigProtoVlanTxEnable_Type.__name__=_K
_LldpXdot1ConfigProtoVlanTxEnable_Object=MibTableColumn
lldpXdot1ConfigProtoVlanTxEnable=_LldpXdot1ConfigProtoVlanTxEnable_Object((1,0,8802,1,1,2,1,5,32962,1,1,3,1,1),_LldpXdot1ConfigProtoVlanTxEnable_Type())
lldpXdot1ConfigProtoVlanTxEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:lldpXdot1ConfigProtoVlanTxEnable.setStatus(_A)
_LldpXdot1ConfigProtocolTable_Object=MibTable
lldpXdot1ConfigProtocolTable=_LldpXdot1ConfigProtocolTable_Object((1,0,8802,1,1,2,1,5,32962,1,1,4))
if mibBuilder.loadTexts:lldpXdot1ConfigProtocolTable.setStatus(_A)
_LldpXdot1ConfigProtocolEntry_Object=MibTableRow
lldpXdot1ConfigProtocolEntry=_LldpXdot1ConfigProtocolEntry_Object((1,0,8802,1,1,2,1,5,32962,1,1,4,1))
if mibBuilder.loadTexts:lldpXdot1ConfigProtocolEntry.setStatus(_A)
class _LldpXdot1ConfigProtocolTxEnable_Type(TruthValue):defaultValue=2
_LldpXdot1ConfigProtocolTxEnable_Type.__name__=_K
_LldpXdot1ConfigProtocolTxEnable_Object=MibTableColumn
lldpXdot1ConfigProtocolTxEnable=_LldpXdot1ConfigProtocolTxEnable_Object((1,0,8802,1,1,2,1,5,32962,1,1,4,1,1),_LldpXdot1ConfigProtocolTxEnable_Type())
lldpXdot1ConfigProtocolTxEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:lldpXdot1ConfigProtocolTxEnable.setStatus(_A)
_LldpXdot1LocalData_ObjectIdentity=ObjectIdentity
lldpXdot1LocalData=_LldpXdot1LocalData_ObjectIdentity((1,0,8802,1,1,2,1,5,32962,1,2))
_LldpXdot1LocTable_Object=MibTable
lldpXdot1LocTable=_LldpXdot1LocTable_Object((1,0,8802,1,1,2,1,5,32962,1,2,1))
if mibBuilder.loadTexts:lldpXdot1LocTable.setStatus(_A)
_LldpXdot1LocEntry_Object=MibTableRow
lldpXdot1LocEntry=_LldpXdot1LocEntry_Object((1,0,8802,1,1,2,1,5,32962,1,2,1,1))
lldpXdot1LocEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:lldpXdot1LocEntry.setStatus(_A)
class _LldpXdot1LocPortVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094))
_LldpXdot1LocPortVlanId_Type.__name__=_E
_LldpXdot1LocPortVlanId_Object=MibTableColumn
lldpXdot1LocPortVlanId=_LldpXdot1LocPortVlanId_Object((1,0,8802,1,1,2,1,5,32962,1,2,1,1,1),_LldpXdot1LocPortVlanId_Type())
lldpXdot1LocPortVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1LocPortVlanId.setStatus(_A)
_LldpXdot1LocProtoVlanTable_Object=MibTable
lldpXdot1LocProtoVlanTable=_LldpXdot1LocProtoVlanTable_Object((1,0,8802,1,1,2,1,5,32962,1,2,2))
if mibBuilder.loadTexts:lldpXdot1LocProtoVlanTable.setStatus(_A)
_LldpXdot1LocProtoVlanEntry_Object=MibTableRow
lldpXdot1LocProtoVlanEntry=_LldpXdot1LocProtoVlanEntry_Object((1,0,8802,1,1,2,1,5,32962,1,2,2,1))
lldpXdot1LocProtoVlanEntry.setIndexNames((0,_C,_G),(0,_B,_O))
if mibBuilder.loadTexts:lldpXdot1LocProtoVlanEntry.setStatus(_A)
class _LldpXdot1LocProtoVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094))
_LldpXdot1LocProtoVlanId_Type.__name__=_E
_LldpXdot1LocProtoVlanId_Object=MibTableColumn
lldpXdot1LocProtoVlanId=_LldpXdot1LocProtoVlanId_Object((1,0,8802,1,1,2,1,5,32962,1,2,2,1,1),_LldpXdot1LocProtoVlanId_Type())
lldpXdot1LocProtoVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpXdot1LocProtoVlanId.setStatus(_A)
_LldpXdot1LocProtoVlanSupported_Type=TruthValue
_LldpXdot1LocProtoVlanSupported_Object=MibTableColumn
lldpXdot1LocProtoVlanSupported=_LldpXdot1LocProtoVlanSupported_Object((1,0,8802,1,1,2,1,5,32962,1,2,2,1,2),_LldpXdot1LocProtoVlanSupported_Type())
lldpXdot1LocProtoVlanSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1LocProtoVlanSupported.setStatus(_A)
_LldpXdot1LocProtoVlanEnabled_Type=TruthValue
_LldpXdot1LocProtoVlanEnabled_Object=MibTableColumn
lldpXdot1LocProtoVlanEnabled=_LldpXdot1LocProtoVlanEnabled_Object((1,0,8802,1,1,2,1,5,32962,1,2,2,1,3),_LldpXdot1LocProtoVlanEnabled_Type())
lldpXdot1LocProtoVlanEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1LocProtoVlanEnabled.setStatus(_A)
_LldpXdot1LocVlanNameTable_Object=MibTable
lldpXdot1LocVlanNameTable=_LldpXdot1LocVlanNameTable_Object((1,0,8802,1,1,2,1,5,32962,1,2,3))
if mibBuilder.loadTexts:lldpXdot1LocVlanNameTable.setStatus(_A)
_LldpXdot1LocVlanNameEntry_Object=MibTableRow
lldpXdot1LocVlanNameEntry=_LldpXdot1LocVlanNameEntry_Object((1,0,8802,1,1,2,1,5,32962,1,2,3,1))
lldpXdot1LocVlanNameEntry.setIndexNames((0,_C,_G),(0,_B,_P))
if mibBuilder.loadTexts:lldpXdot1LocVlanNameEntry.setStatus(_A)
_LldpXdot1LocVlanId_Type=VlanId
_LldpXdot1LocVlanId_Object=MibTableColumn
lldpXdot1LocVlanId=_LldpXdot1LocVlanId_Object((1,0,8802,1,1,2,1,5,32962,1,2,3,1,1),_LldpXdot1LocVlanId_Type())
lldpXdot1LocVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpXdot1LocVlanId.setStatus(_A)
class _LldpXdot1LocVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_LldpXdot1LocVlanName_Type.__name__=_N
_LldpXdot1LocVlanName_Object=MibTableColumn
lldpXdot1LocVlanName=_LldpXdot1LocVlanName_Object((1,0,8802,1,1,2,1,5,32962,1,2,3,1,2),_LldpXdot1LocVlanName_Type())
lldpXdot1LocVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1LocVlanName.setStatus(_A)
_LldpXdot1LocProtocolTable_Object=MibTable
lldpXdot1LocProtocolTable=_LldpXdot1LocProtocolTable_Object((1,0,8802,1,1,2,1,5,32962,1,2,4))
if mibBuilder.loadTexts:lldpXdot1LocProtocolTable.setStatus(_A)
_LldpXdot1LocProtocolEntry_Object=MibTableRow
lldpXdot1LocProtocolEntry=_LldpXdot1LocProtocolEntry_Object((1,0,8802,1,1,2,1,5,32962,1,2,4,1))
lldpXdot1LocProtocolEntry.setIndexNames((0,_C,_G),(0,_B,_Q))
if mibBuilder.loadTexts:lldpXdot1LocProtocolEntry.setStatus(_A)
class _LldpXdot1LocProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpXdot1LocProtocolIndex_Type.__name__=_E
_LldpXdot1LocProtocolIndex_Object=MibTableColumn
lldpXdot1LocProtocolIndex=_LldpXdot1LocProtocolIndex_Object((1,0,8802,1,1,2,1,5,32962,1,2,4,1,1),_LldpXdot1LocProtocolIndex_Type())
lldpXdot1LocProtocolIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpXdot1LocProtocolIndex.setStatus(_A)
class _LldpXdot1LocProtocolId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_LldpXdot1LocProtocolId_Type.__name__=_M
_LldpXdot1LocProtocolId_Object=MibTableColumn
lldpXdot1LocProtocolId=_LldpXdot1LocProtocolId_Object((1,0,8802,1,1,2,1,5,32962,1,2,4,1,2),_LldpXdot1LocProtocolId_Type())
lldpXdot1LocProtocolId.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1LocProtocolId.setStatus(_A)
_LldpXdot1RemoteData_ObjectIdentity=ObjectIdentity
lldpXdot1RemoteData=_LldpXdot1RemoteData_ObjectIdentity((1,0,8802,1,1,2,1,5,32962,1,3))
_LldpXdot1RemTable_Object=MibTable
lldpXdot1RemTable=_LldpXdot1RemTable_Object((1,0,8802,1,1,2,1,5,32962,1,3,1))
if mibBuilder.loadTexts:lldpXdot1RemTable.setStatus(_A)
_LldpXdot1RemEntry_Object=MibTableRow
lldpXdot1RemEntry=_LldpXdot1RemEntry_Object((1,0,8802,1,1,2,1,5,32962,1,3,1,1))
lldpXdot1RemEntry.setIndexNames((0,_C,_J),(0,_C,_I),(0,_C,_H))
if mibBuilder.loadTexts:lldpXdot1RemEntry.setStatus(_A)
class _LldpXdot1RemPortVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094))
_LldpXdot1RemPortVlanId_Type.__name__=_E
_LldpXdot1RemPortVlanId_Object=MibTableColumn
lldpXdot1RemPortVlanId=_LldpXdot1RemPortVlanId_Object((1,0,8802,1,1,2,1,5,32962,1,3,1,1,1),_LldpXdot1RemPortVlanId_Type())
lldpXdot1RemPortVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1RemPortVlanId.setStatus(_A)
_LldpXdot1RemProtoVlanTable_Object=MibTable
lldpXdot1RemProtoVlanTable=_LldpXdot1RemProtoVlanTable_Object((1,0,8802,1,1,2,1,5,32962,1,3,2))
if mibBuilder.loadTexts:lldpXdot1RemProtoVlanTable.setStatus(_A)
_LldpXdot1RemProtoVlanEntry_Object=MibTableRow
lldpXdot1RemProtoVlanEntry=_LldpXdot1RemProtoVlanEntry_Object((1,0,8802,1,1,2,1,5,32962,1,3,2,1))
lldpXdot1RemProtoVlanEntry.setIndexNames((0,_C,_J),(0,_C,_I),(0,_C,_H),(0,_B,_R))
if mibBuilder.loadTexts:lldpXdot1RemProtoVlanEntry.setStatus(_A)
class _LldpXdot1RemProtoVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094))
_LldpXdot1RemProtoVlanId_Type.__name__=_E
_LldpXdot1RemProtoVlanId_Object=MibTableColumn
lldpXdot1RemProtoVlanId=_LldpXdot1RemProtoVlanId_Object((1,0,8802,1,1,2,1,5,32962,1,3,2,1,1),_LldpXdot1RemProtoVlanId_Type())
lldpXdot1RemProtoVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpXdot1RemProtoVlanId.setStatus(_A)
_LldpXdot1RemProtoVlanSupported_Type=TruthValue
_LldpXdot1RemProtoVlanSupported_Object=MibTableColumn
lldpXdot1RemProtoVlanSupported=_LldpXdot1RemProtoVlanSupported_Object((1,0,8802,1,1,2,1,5,32962,1,3,2,1,2),_LldpXdot1RemProtoVlanSupported_Type())
lldpXdot1RemProtoVlanSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1RemProtoVlanSupported.setStatus(_A)
_LldpXdot1RemProtoVlanEnabled_Type=TruthValue
_LldpXdot1RemProtoVlanEnabled_Object=MibTableColumn
lldpXdot1RemProtoVlanEnabled=_LldpXdot1RemProtoVlanEnabled_Object((1,0,8802,1,1,2,1,5,32962,1,3,2,1,3),_LldpXdot1RemProtoVlanEnabled_Type())
lldpXdot1RemProtoVlanEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1RemProtoVlanEnabled.setStatus(_A)
_LldpXdot1RemVlanNameTable_Object=MibTable
lldpXdot1RemVlanNameTable=_LldpXdot1RemVlanNameTable_Object((1,0,8802,1,1,2,1,5,32962,1,3,3))
if mibBuilder.loadTexts:lldpXdot1RemVlanNameTable.setStatus(_A)
_LldpXdot1RemVlanNameEntry_Object=MibTableRow
lldpXdot1RemVlanNameEntry=_LldpXdot1RemVlanNameEntry_Object((1,0,8802,1,1,2,1,5,32962,1,3,3,1))
lldpXdot1RemVlanNameEntry.setIndexNames((0,_C,_J),(0,_C,_I),(0,_C,_H),(0,_B,_S))
if mibBuilder.loadTexts:lldpXdot1RemVlanNameEntry.setStatus(_A)
_LldpXdot1RemVlanId_Type=VlanId
_LldpXdot1RemVlanId_Object=MibTableColumn
lldpXdot1RemVlanId=_LldpXdot1RemVlanId_Object((1,0,8802,1,1,2,1,5,32962,1,3,3,1,1),_LldpXdot1RemVlanId_Type())
lldpXdot1RemVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpXdot1RemVlanId.setStatus(_A)
class _LldpXdot1RemVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_LldpXdot1RemVlanName_Type.__name__=_N
_LldpXdot1RemVlanName_Object=MibTableColumn
lldpXdot1RemVlanName=_LldpXdot1RemVlanName_Object((1,0,8802,1,1,2,1,5,32962,1,3,3,1,2),_LldpXdot1RemVlanName_Type())
lldpXdot1RemVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1RemVlanName.setStatus(_A)
_LldpXdot1RemProtocolTable_Object=MibTable
lldpXdot1RemProtocolTable=_LldpXdot1RemProtocolTable_Object((1,0,8802,1,1,2,1,5,32962,1,3,4))
if mibBuilder.loadTexts:lldpXdot1RemProtocolTable.setStatus(_A)
_LldpXdot1RemProtocolEntry_Object=MibTableRow
lldpXdot1RemProtocolEntry=_LldpXdot1RemProtocolEntry_Object((1,0,8802,1,1,2,1,5,32962,1,3,4,1))
lldpXdot1RemProtocolEntry.setIndexNames((0,_C,_J),(0,_C,_I),(0,_C,_H),(0,_B,_T))
if mibBuilder.loadTexts:lldpXdot1RemProtocolEntry.setStatus(_A)
class _LldpXdot1RemProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LldpXdot1RemProtocolIndex_Type.__name__=_E
_LldpXdot1RemProtocolIndex_Object=MibTableColumn
lldpXdot1RemProtocolIndex=_LldpXdot1RemProtocolIndex_Object((1,0,8802,1,1,2,1,5,32962,1,3,4,1,1),_LldpXdot1RemProtocolIndex_Type())
lldpXdot1RemProtocolIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:lldpXdot1RemProtocolIndex.setStatus(_A)
class _LldpXdot1RemProtocolId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_LldpXdot1RemProtocolId_Type.__name__=_M
_LldpXdot1RemProtocolId_Object=MibTableColumn
lldpXdot1RemProtocolId=_LldpXdot1RemProtocolId_Object((1,0,8802,1,1,2,1,5,32962,1,3,4,1,2),_LldpXdot1RemProtocolId_Type())
lldpXdot1RemProtocolId.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1RemProtocolId.setStatus(_A)
_LldpXdot1Conformance_ObjectIdentity=ObjectIdentity
lldpXdot1Conformance=_LldpXdot1Conformance_ObjectIdentity((1,0,8802,1,1,2,1,5,32962,2))
_LldpXdot1Compliances_ObjectIdentity=ObjectIdentity
lldpXdot1Compliances=_LldpXdot1Compliances_ObjectIdentity((1,0,8802,1,1,2,1,5,32962,2,1))
_LldpXdot1Groups_ObjectIdentity=ObjectIdentity
lldpXdot1Groups=_LldpXdot1Groups_ObjectIdentity((1,0,8802,1,1,2,1,5,32962,2,2))
lldpPortConfigEntry.registerAugmentions((_B,_U))
lldpXdot1ConfigPortVlanEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpXdot1LocVlanNameEntry.registerAugmentions((_B,_V))
lldpXdot1ConfigVlanNameEntry.setIndexNames(*lldpXdot1LocVlanNameEntry.getIndexNames())
lldpXdot1LocProtoVlanEntry.registerAugmentions((_B,_W))
lldpXdot1ConfigProtoVlanEntry.setIndexNames(*lldpXdot1LocProtoVlanEntry.getIndexNames())
lldpXdot1LocProtocolEntry.registerAugmentions((_B,_X))
lldpXdot1ConfigProtocolEntry.setIndexNames(*lldpXdot1LocProtocolEntry.getIndexNames())
lldpXdot1ConfigGroup=ObjectGroup((1,0,8802,1,1,2,1,5,32962,2,2,1))
lldpXdot1ConfigGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:lldpXdot1ConfigGroup.setStatus(_A)
lldpXdot1LocSysGroup=ObjectGroup((1,0,8802,1,1,2,1,5,32962,2,2,2))
lldpXdot1LocSysGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:lldpXdot1LocSysGroup.setStatus(_A)
lldpXdot1RemSysGroup=ObjectGroup((1,0,8802,1,1,2,1,5,32962,2,2,3))
lldpXdot1RemSysGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:lldpXdot1RemSysGroup.setStatus(_A)
lldpXdot1Compliance=ModuleCompliance((1,0,8802,1,1,2,1,5,32962,2,1,1))
lldpXdot1Compliance.setObjects(*((_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:lldpXdot1Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lldpXdot1MIB':lldpXdot1MIB,'lldpXdot1Objects':lldpXdot1Objects,'lldpXdot1Config':lldpXdot1Config,'lldpXdot1ConfigPortVlanTable':lldpXdot1ConfigPortVlanTable,_U:lldpXdot1ConfigPortVlanEntry,_Y:lldpXdot1ConfigPortVlanTxEnable,'lldpXdot1ConfigVlanNameTable':lldpXdot1ConfigVlanNameTable,_V:lldpXdot1ConfigVlanNameEntry,_Z:lldpXdot1ConfigVlanNameTxEnable,'lldpXdot1ConfigProtoVlanTable':lldpXdot1ConfigProtoVlanTable,_W:lldpXdot1ConfigProtoVlanEntry,_a:lldpXdot1ConfigProtoVlanTxEnable,'lldpXdot1ConfigProtocolTable':lldpXdot1ConfigProtocolTable,_X:lldpXdot1ConfigProtocolEntry,_b:lldpXdot1ConfigProtocolTxEnable,'lldpXdot1LocalData':lldpXdot1LocalData,'lldpXdot1LocTable':lldpXdot1LocTable,'lldpXdot1LocEntry':lldpXdot1LocEntry,_c:lldpXdot1LocPortVlanId,'lldpXdot1LocProtoVlanTable':lldpXdot1LocProtoVlanTable,'lldpXdot1LocProtoVlanEntry':lldpXdot1LocProtoVlanEntry,_O:lldpXdot1LocProtoVlanId,_d:lldpXdot1LocProtoVlanSupported,_e:lldpXdot1LocProtoVlanEnabled,'lldpXdot1LocVlanNameTable':lldpXdot1LocVlanNameTable,'lldpXdot1LocVlanNameEntry':lldpXdot1LocVlanNameEntry,_P:lldpXdot1LocVlanId,_f:lldpXdot1LocVlanName,'lldpXdot1LocProtocolTable':lldpXdot1LocProtocolTable,'lldpXdot1LocProtocolEntry':lldpXdot1LocProtocolEntry,_Q:lldpXdot1LocProtocolIndex,_g:lldpXdot1LocProtocolId,'lldpXdot1RemoteData':lldpXdot1RemoteData,'lldpXdot1RemTable':lldpXdot1RemTable,'lldpXdot1RemEntry':lldpXdot1RemEntry,_h:lldpXdot1RemPortVlanId,'lldpXdot1RemProtoVlanTable':lldpXdot1RemProtoVlanTable,'lldpXdot1RemProtoVlanEntry':lldpXdot1RemProtoVlanEntry,_R:lldpXdot1RemProtoVlanId,_i:lldpXdot1RemProtoVlanSupported,_j:lldpXdot1RemProtoVlanEnabled,'lldpXdot1RemVlanNameTable':lldpXdot1RemVlanNameTable,'lldpXdot1RemVlanNameEntry':lldpXdot1RemVlanNameEntry,_S:lldpXdot1RemVlanId,_k:lldpXdot1RemVlanName,'lldpXdot1RemProtocolTable':lldpXdot1RemProtocolTable,'lldpXdot1RemProtocolEntry':lldpXdot1RemProtocolEntry,_T:lldpXdot1RemProtocolIndex,_l:lldpXdot1RemProtocolId,'lldpXdot1Conformance':lldpXdot1Conformance,'lldpXdot1Compliances':lldpXdot1Compliances,'lldpXdot1Compliance':lldpXdot1Compliance,'lldpXdot1Groups':lldpXdot1Groups,_m:lldpXdot1ConfigGroup,_n:lldpXdot1LocSysGroup,_o:lldpXdot1RemSysGroup})