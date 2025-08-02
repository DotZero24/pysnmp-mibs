_x='juniAddressPoolGroup5'
_w='juniAddressPoolGroup4'
_v='juniAddressPoolGroup2'
_u='juniAddressPoolGroup'
_t='juniAddressPoolNoAddresses'
_s='juniAddressPoolAbatedAddrUtil'
_r='juniAddressPoolHighAddrUtil'
_q='juniAddressSharedPoolInUse'
_p='juniAddressSharedPoolDhcpPoolName'
_o='juniAddressSharedPoolName'
_n='juniAddressSharedPoolRowStatus'
_m='juniAddressAliasPoolName'
_l='juniAddressAliasRowStatus'
_k='juniAddressSharedPoolIndex'
_j='juniAddressAliasName'
_i='juniAddressPoolProfileIndex'
_h='TruthValue'
_g='juniAddressPoolGroup3'
_f='juniAddressPoolNextPoolProfileIndex'
_e='juniAddressPoolIndex'
_d='DisplayString'
_c='juniAddressAliasGroup'
_b='juniAddressPoolProfileInUse'
_a='juniAddressPoolProfileSize'
_Z='juniAddressPoolProfileEnd'
_Y='juniAddressPoolProfileStart'
_X='juniAddressPoolProfileRowStatus'
_W='juniAddressPoolEnd'
_V='juniAddressPoolStart'
_U='not-accessible'
_T='juniRouterName'
_S='Juniper-ROUTER-MIB'
_R='OctetString'
_Q='juniAddressPoolTrapEnable'
_P='juniAddressPoolAbatedUtilThreshold'
_O='juniAddressPoolHighUtilThreshold'
_N='deprecated'
_M='juniAddressPoolTrapGroup'
_L='juniAddressPoolNextPoolIndex'
_K='juniAddressPoolInUse'
_J='juniAddressPoolRowStatus'
_I='juniAddressPoolUtilPct'
_H='juniAddressPoolSize'
_G='obsolete'
_F='read-only'
_E='juniAddressPoolName'
_D='Integer32'
_C='read-create'
_B='current'
_A='Juniper-ADDRESS-POOL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
juniRouterName,=mibBuilder.importSymbols(_S,_T)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_d,'PhysAddress','RowStatus','TextualConvention',_h)
juniAddressPoolMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,21))
if mibBuilder.loadTexts:juniAddressPoolMIB.setRevisions(('2005-02-11 21:35','2004-09-17 22:37','2003-11-03 22:37','2002-09-16 21:44','2002-05-06 18:38','2001-05-02 11:57','2001-04-27 15:00','1999-06-01 00:00'))
_JuniAddressPoolObjects_ObjectIdentity=ObjectIdentity
juniAddressPoolObjects=_JuniAddressPoolObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,21,1))
_JuniAddressPool_ObjectIdentity=ObjectIdentity
juniAddressPool=_JuniAddressPool_ObjectIdentity((1,3,6,1,4,1,4874,2,2,21,1,1))
_JuniAddressPoolTable_Object=MibTable
juniAddressPoolTable=_JuniAddressPoolTable_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1))
if mibBuilder.loadTexts:juniAddressPoolTable.setStatus(_B)
_JuniAddressPoolEntry_Object=MibTableRow
juniAddressPoolEntry=_JuniAddressPoolEntry_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1,1))
juniAddressPoolEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:juniAddressPoolEntry.setStatus(_B)
class _JuniAddressPoolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JuniAddressPoolIndex_Type.__name__=_D
_JuniAddressPoolIndex_Object=MibTableColumn
juniAddressPoolIndex=_JuniAddressPoolIndex_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1,1,1),_JuniAddressPoolIndex_Type())
juniAddressPoolIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:juniAddressPoolIndex.setStatus(_B)
_JuniAddressPoolRowStatus_Type=RowStatus
_JuniAddressPoolRowStatus_Object=MibTableColumn
juniAddressPoolRowStatus=_JuniAddressPoolRowStatus_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1,1,2),_JuniAddressPoolRowStatus_Type())
juniAddressPoolRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressPoolRowStatus.setStatus(_B)
class _JuniAddressPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_JuniAddressPoolName_Type.__name__=_R
_JuniAddressPoolName_Object=MibTableColumn
juniAddressPoolName=_JuniAddressPoolName_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1,1,3),_JuniAddressPoolName_Type())
juniAddressPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressPoolName.setStatus(_B)
_JuniAddressPoolStart_Type=IpAddress
_JuniAddressPoolStart_Object=MibTableColumn
juniAddressPoolStart=_JuniAddressPoolStart_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1,1,4),_JuniAddressPoolStart_Type())
juniAddressPoolStart.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressPoolStart.setStatus(_N)
_JuniAddressPoolEnd_Type=IpAddress
_JuniAddressPoolEnd_Object=MibTableColumn
juniAddressPoolEnd=_JuniAddressPoolEnd_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1,1,5),_JuniAddressPoolEnd_Type())
juniAddressPoolEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressPoolEnd.setStatus(_N)
_JuniAddressPoolSize_Type=Integer32
_JuniAddressPoolSize_Object=MibTableColumn
juniAddressPoolSize=_JuniAddressPoolSize_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1,1,6),_JuniAddressPoolSize_Type())
juniAddressPoolSize.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAddressPoolSize.setStatus(_N)
_JuniAddressPoolInUse_Type=Integer32
_JuniAddressPoolInUse_Object=MibTableColumn
juniAddressPoolInUse=_JuniAddressPoolInUse_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1,1,7),_JuniAddressPoolInUse_Type())
juniAddressPoolInUse.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAddressPoolInUse.setStatus(_N)
class _JuniAddressPoolHighUtilThreshold_Type(Integer32):defaultValue=85;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_JuniAddressPoolHighUtilThreshold_Type.__name__=_D
_JuniAddressPoolHighUtilThreshold_Object=MibTableColumn
juniAddressPoolHighUtilThreshold=_JuniAddressPoolHighUtilThreshold_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1,1,8),_JuniAddressPoolHighUtilThreshold_Type())
juniAddressPoolHighUtilThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressPoolHighUtilThreshold.setStatus(_B)
class _JuniAddressPoolAbatedUtilThreshold_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_JuniAddressPoolAbatedUtilThreshold_Type.__name__=_D
_JuniAddressPoolAbatedUtilThreshold_Object=MibTableColumn
juniAddressPoolAbatedUtilThreshold=_JuniAddressPoolAbatedUtilThreshold_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1,1,9),_JuniAddressPoolAbatedUtilThreshold_Type())
juniAddressPoolAbatedUtilThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressPoolAbatedUtilThreshold.setStatus(_B)
class _JuniAddressPoolUtilPct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_JuniAddressPoolUtilPct_Type.__name__=_D
_JuniAddressPoolUtilPct_Object=MibTableColumn
juniAddressPoolUtilPct=_JuniAddressPoolUtilPct_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1,1,10),_JuniAddressPoolUtilPct_Type())
juniAddressPoolUtilPct.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAddressPoolUtilPct.setStatus(_B)
class _JuniAddressPoolTrapEnable_Type(TruthValue):defaultValue=2
_JuniAddressPoolTrapEnable_Type.__name__=_h
_JuniAddressPoolTrapEnable_Object=MibTableColumn
juniAddressPoolTrapEnable=_JuniAddressPoolTrapEnable_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1,1,11),_JuniAddressPoolTrapEnable_Type())
juniAddressPoolTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressPoolTrapEnable.setStatus(_B)
class _JuniAddressPoolNextPoolProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniAddressPoolNextPoolProfileIndex_Type.__name__=_D
_JuniAddressPoolNextPoolProfileIndex_Object=MibTableColumn
juniAddressPoolNextPoolProfileIndex=_JuniAddressPoolNextPoolProfileIndex_Object((1,3,6,1,4,1,4874,2,2,21,1,1,1,1,12),_JuniAddressPoolNextPoolProfileIndex_Type())
juniAddressPoolNextPoolProfileIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAddressPoolNextPoolProfileIndex.setStatus(_B)
class _JuniAddressPoolNextPoolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniAddressPoolNextPoolIndex_Type.__name__=_D
_JuniAddressPoolNextPoolIndex_Object=MibScalar
juniAddressPoolNextPoolIndex=_JuniAddressPoolNextPoolIndex_Object((1,3,6,1,4,1,4874,2,2,21,1,1,2),_JuniAddressPoolNextPoolIndex_Type())
juniAddressPoolNextPoolIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAddressPoolNextPoolIndex.setStatus(_B)
_JuniAddressPoolProfileTable_Object=MibTable
juniAddressPoolProfileTable=_JuniAddressPoolProfileTable_Object((1,3,6,1,4,1,4874,2,2,21,1,1,3))
if mibBuilder.loadTexts:juniAddressPoolProfileTable.setStatus(_B)
_JuniAddressPoolProfileEntry_Object=MibTableRow
juniAddressPoolProfileEntry=_JuniAddressPoolProfileEntry_Object((1,3,6,1,4,1,4874,2,2,21,1,1,3,1))
juniAddressPoolProfileEntry.setIndexNames((0,_A,_e),(0,_A,_i))
if mibBuilder.loadTexts:juniAddressPoolProfileEntry.setStatus(_B)
class _JuniAddressPoolProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JuniAddressPoolProfileIndex_Type.__name__=_D
_JuniAddressPoolProfileIndex_Object=MibTableColumn
juniAddressPoolProfileIndex=_JuniAddressPoolProfileIndex_Object((1,3,6,1,4,1,4874,2,2,21,1,1,3,1,1),_JuniAddressPoolProfileIndex_Type())
juniAddressPoolProfileIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:juniAddressPoolProfileIndex.setStatus(_B)
_JuniAddressPoolProfileRowStatus_Type=RowStatus
_JuniAddressPoolProfileRowStatus_Object=MibTableColumn
juniAddressPoolProfileRowStatus=_JuniAddressPoolProfileRowStatus_Object((1,3,6,1,4,1,4874,2,2,21,1,1,3,1,2),_JuniAddressPoolProfileRowStatus_Type())
juniAddressPoolProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressPoolProfileRowStatus.setStatus(_B)
_JuniAddressPoolProfileStart_Type=IpAddress
_JuniAddressPoolProfileStart_Object=MibTableColumn
juniAddressPoolProfileStart=_JuniAddressPoolProfileStart_Object((1,3,6,1,4,1,4874,2,2,21,1,1,3,1,3),_JuniAddressPoolProfileStart_Type())
juniAddressPoolProfileStart.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressPoolProfileStart.setStatus(_B)
_JuniAddressPoolProfileEnd_Type=IpAddress
_JuniAddressPoolProfileEnd_Object=MibTableColumn
juniAddressPoolProfileEnd=_JuniAddressPoolProfileEnd_Object((1,3,6,1,4,1,4874,2,2,21,1,1,3,1,4),_JuniAddressPoolProfileEnd_Type())
juniAddressPoolProfileEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressPoolProfileEnd.setStatus(_B)
_JuniAddressPoolProfileSize_Type=Integer32
_JuniAddressPoolProfileSize_Object=MibTableColumn
juniAddressPoolProfileSize=_JuniAddressPoolProfileSize_Object((1,3,6,1,4,1,4874,2,2,21,1,1,3,1,5),_JuniAddressPoolProfileSize_Type())
juniAddressPoolProfileSize.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAddressPoolProfileSize.setStatus(_B)
_JuniAddressPoolProfileInUse_Type=Integer32
_JuniAddressPoolProfileInUse_Object=MibTableColumn
juniAddressPoolProfileInUse=_JuniAddressPoolProfileInUse_Object((1,3,6,1,4,1,4874,2,2,21,1,1,3,1,6),_JuniAddressPoolProfileInUse_Type())
juniAddressPoolProfileInUse.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAddressPoolProfileInUse.setStatus(_B)
_JuniAddressAliasTable_Object=MibTable
juniAddressAliasTable=_JuniAddressAliasTable_Object((1,3,6,1,4,1,4874,2,2,21,1,1,4))
if mibBuilder.loadTexts:juniAddressAliasTable.setStatus(_B)
_JuniAddressAliasEntry_Object=MibTableRow
juniAddressAliasEntry=_JuniAddressAliasEntry_Object((1,3,6,1,4,1,4874,2,2,21,1,1,4,1))
juniAddressAliasEntry.setIndexNames((1,_A,_j))
if mibBuilder.loadTexts:juniAddressAliasEntry.setStatus(_B)
class _JuniAddressAliasName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_JuniAddressAliasName_Type.__name__=_d
_JuniAddressAliasName_Object=MibTableColumn
juniAddressAliasName=_JuniAddressAliasName_Object((1,3,6,1,4,1,4874,2,2,21,1,1,4,1,1),_JuniAddressAliasName_Type())
juniAddressAliasName.setMaxAccess(_U)
if mibBuilder.loadTexts:juniAddressAliasName.setStatus(_B)
_JuniAddressAliasRowStatus_Type=RowStatus
_JuniAddressAliasRowStatus_Object=MibTableColumn
juniAddressAliasRowStatus=_JuniAddressAliasRowStatus_Object((1,3,6,1,4,1,4874,2,2,21,1,1,4,1,2),_JuniAddressAliasRowStatus_Type())
juniAddressAliasRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressAliasRowStatus.setStatus(_B)
class _JuniAddressAliasPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_JuniAddressAliasPoolName_Type.__name__=_d
_JuniAddressAliasPoolName_Object=MibTableColumn
juniAddressAliasPoolName=_JuniAddressAliasPoolName_Object((1,3,6,1,4,1,4874,2,2,21,1,1,4,1,3),_JuniAddressAliasPoolName_Type())
juniAddressAliasPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressAliasPoolName.setStatus(_B)
_JuniAddressSharedPoolTable_Object=MibTable
juniAddressSharedPoolTable=_JuniAddressSharedPoolTable_Object((1,3,6,1,4,1,4874,2,2,21,1,1,5))
if mibBuilder.loadTexts:juniAddressSharedPoolTable.setStatus(_B)
_JuniAddressSharedPoolEntry_Object=MibTableRow
juniAddressSharedPoolEntry=_JuniAddressSharedPoolEntry_Object((1,3,6,1,4,1,4874,2,2,21,1,1,5,1))
juniAddressSharedPoolEntry.setIndexNames((0,_A,_k))
if mibBuilder.loadTexts:juniAddressSharedPoolEntry.setStatus(_B)
class _JuniAddressSharedPoolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JuniAddressSharedPoolIndex_Type.__name__=_D
_JuniAddressSharedPoolIndex_Object=MibTableColumn
juniAddressSharedPoolIndex=_JuniAddressSharedPoolIndex_Object((1,3,6,1,4,1,4874,2,2,21,1,1,5,1,1),_JuniAddressSharedPoolIndex_Type())
juniAddressSharedPoolIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:juniAddressSharedPoolIndex.setStatus(_B)
_JuniAddressSharedPoolRowStatus_Type=RowStatus
_JuniAddressSharedPoolRowStatus_Object=MibTableColumn
juniAddressSharedPoolRowStatus=_JuniAddressSharedPoolRowStatus_Object((1,3,6,1,4,1,4874,2,2,21,1,1,5,1,2),_JuniAddressSharedPoolRowStatus_Type())
juniAddressSharedPoolRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressSharedPoolRowStatus.setStatus(_B)
class _JuniAddressSharedPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_JuniAddressSharedPoolName_Type.__name__=_R
_JuniAddressSharedPoolName_Object=MibTableColumn
juniAddressSharedPoolName=_JuniAddressSharedPoolName_Object((1,3,6,1,4,1,4874,2,2,21,1,1,5,1,3),_JuniAddressSharedPoolName_Type())
juniAddressSharedPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressSharedPoolName.setStatus(_B)
class _JuniAddressSharedPoolDhcpPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_JuniAddressSharedPoolDhcpPoolName_Type.__name__=_R
_JuniAddressSharedPoolDhcpPoolName_Object=MibTableColumn
juniAddressSharedPoolDhcpPoolName=_JuniAddressSharedPoolDhcpPoolName_Object((1,3,6,1,4,1,4874,2,2,21,1,1,5,1,4),_JuniAddressSharedPoolDhcpPoolName_Type())
juniAddressSharedPoolDhcpPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAddressSharedPoolDhcpPoolName.setStatus(_B)
_JuniAddressSharedPoolInUse_Type=Integer32
_JuniAddressSharedPoolInUse_Object=MibTableColumn
juniAddressSharedPoolInUse=_JuniAddressSharedPoolInUse_Object((1,3,6,1,4,1,4874,2,2,21,1,1,5,1,5),_JuniAddressSharedPoolInUse_Type())
juniAddressSharedPoolInUse.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAddressSharedPoolInUse.setStatus(_B)
_JuniAddressPoolTraps_ObjectIdentity=ObjectIdentity
juniAddressPoolTraps=_JuniAddressPoolTraps_ObjectIdentity((1,3,6,1,4,1,4874,2,2,21,3))
_JuniAddressPoolTrapPrefix_ObjectIdentity=ObjectIdentity
juniAddressPoolTrapPrefix=_JuniAddressPoolTrapPrefix_ObjectIdentity((1,3,6,1,4,1,4874,2,2,21,3,0))
_JuniAddressPoolMIBConformance_ObjectIdentity=ObjectIdentity
juniAddressPoolMIBConformance=_JuniAddressPoolMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,21,4))
_JuniAddressPoolMIBCompliances_ObjectIdentity=ObjectIdentity
juniAddressPoolMIBCompliances=_JuniAddressPoolMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,21,4,1))
_JuniAddressPoolMIBGroups_ObjectIdentity=ObjectIdentity
juniAddressPoolMIBGroups=_JuniAddressPoolMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,21,4,2))
juniAddressPoolGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,21,4,2,1))
juniAddressPoolGroup.setObjects(*((_A,_J),(_A,_E),(_A,_V),(_A,_W),(_A,_H),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:juniAddressPoolGroup.setStatus(_G)
juniAddressPoolGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,21,4,2,2))
juniAddressPoolGroup2.setObjects(*((_A,_J),(_A,_E),(_A,_V),(_A,_W),(_A,_H),(_A,_K),(_A,_L),(_A,_O),(_A,_P),(_A,_I),(_A,_Q)))
if mibBuilder.loadTexts:juniAddressPoolGroup2.setStatus(_G)
juniAddressPoolGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,21,4,2,4))
juniAddressPoolGroup3.setObjects(*((_A,_J),(_A,_E),(_A,_L),(_A,_O),(_A,_P),(_A,_I),(_A,_Q),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:juniAddressPoolGroup3.setStatus(_B)
juniAddressPoolDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,21,4,2,5))
juniAddressPoolDeprecatedGroup.setObjects(*((_A,_V),(_A,_W),(_A,_H),(_A,_K)))
if mibBuilder.loadTexts:juniAddressPoolDeprecatedGroup.setStatus(_N)
juniAddressAliasGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,21,4,2,6))
juniAddressAliasGroup.setObjects(*((_A,_l),(_A,_m)))
if mibBuilder.loadTexts:juniAddressAliasGroup.setStatus(_B)
juniAddressPoolGroup4=ObjectGroup((1,3,6,1,4,1,4874,2,2,21,4,2,7))
juniAddressPoolGroup4.setObjects(*((_A,_J),(_A,_E),(_A,_L),(_A,_O),(_A,_P),(_A,_I),(_A,_Q),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_f)))
if mibBuilder.loadTexts:juniAddressPoolGroup4.setStatus(_G)
juniAddressPoolGroup5=ObjectGroup((1,3,6,1,4,1,4874,2,2,21,4,2,8))
juniAddressPoolGroup5.setObjects(*((_A,_J),(_A,_E),(_A,_L),(_A,_O),(_A,_P),(_A,_I),(_A,_Q),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_f),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:juniAddressPoolGroup5.setStatus(_B)
juniAddressPoolHighAddrUtil=NotificationType((1,3,6,1,4,1,4874,2,2,21,3,0,1))
juniAddressPoolHighAddrUtil.setObjects(*((_S,_T),(_A,_E),(_A,_H),(_A,_K),(_A,_I)))
if mibBuilder.loadTexts:juniAddressPoolHighAddrUtil.setStatus(_B)
juniAddressPoolAbatedAddrUtil=NotificationType((1,3,6,1,4,1,4874,2,2,21,3,0,2))
juniAddressPoolAbatedAddrUtil.setObjects(*((_S,_T),(_A,_E),(_A,_H),(_A,_K),(_A,_I)))
if mibBuilder.loadTexts:juniAddressPoolAbatedAddrUtil.setStatus(_B)
juniAddressPoolNoAddresses=NotificationType((1,3,6,1,4,1,4874,2,2,21,3,0,3))
juniAddressPoolNoAddresses.setObjects(*((_S,_T),(_A,_E),(_A,_H)))
if mibBuilder.loadTexts:juniAddressPoolNoAddresses.setStatus(_B)
juniAddressPoolTrapGroup=NotificationGroup((1,3,6,1,4,1,4874,2,2,21,4,2,3))
juniAddressPoolTrapGroup.setObjects(*((_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:juniAddressPoolTrapGroup.setStatus(_B)
juniAddressPoolCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,21,4,1,1))
juniAddressPoolCompliance.setObjects((_A,_u))
if mibBuilder.loadTexts:juniAddressPoolCompliance.setStatus(_G)
juniAddressPoolCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,21,4,1,2))
juniAddressPoolCompliance2.setObjects(*((_A,_v),(_A,_M)))
if mibBuilder.loadTexts:juniAddressPoolCompliance2.setStatus(_G)
juniAddressPoolCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,21,4,1,3))
juniAddressPoolCompliance3.setObjects(*((_A,_g),(_A,_M)))
if mibBuilder.loadTexts:juniAddressPoolCompliance3.setStatus(_G)
juniAddressPoolCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,21,4,1,4))
juniAddressPoolCompliance4.setObjects(*((_A,_g),(_A,_M),(_A,_c)))
if mibBuilder.loadTexts:juniAddressPoolCompliance4.setStatus(_G)
juniAddressPoolCompliance5=ModuleCompliance((1,3,6,1,4,1,4874,2,2,21,4,1,5))
juniAddressPoolCompliance5.setObjects(*((_A,_w),(_A,_M),(_A,_c)))
if mibBuilder.loadTexts:juniAddressPoolCompliance5.setStatus(_G)
juniAddressPoolCompliance6=ModuleCompliance((1,3,6,1,4,1,4874,2,2,21,4,1,6))
juniAddressPoolCompliance6.setObjects(*((_A,_x),(_A,_M),(_A,_c)))
if mibBuilder.loadTexts:juniAddressPoolCompliance6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniAddressPoolMIB':juniAddressPoolMIB,'juniAddressPoolObjects':juniAddressPoolObjects,'juniAddressPool':juniAddressPool,'juniAddressPoolTable':juniAddressPoolTable,'juniAddressPoolEntry':juniAddressPoolEntry,_e:juniAddressPoolIndex,_J:juniAddressPoolRowStatus,_E:juniAddressPoolName,_V:juniAddressPoolStart,_W:juniAddressPoolEnd,_H:juniAddressPoolSize,_K:juniAddressPoolInUse,_O:juniAddressPoolHighUtilThreshold,_P:juniAddressPoolAbatedUtilThreshold,_I:juniAddressPoolUtilPct,_Q:juniAddressPoolTrapEnable,_f:juniAddressPoolNextPoolProfileIndex,_L:juniAddressPoolNextPoolIndex,'juniAddressPoolProfileTable':juniAddressPoolProfileTable,'juniAddressPoolProfileEntry':juniAddressPoolProfileEntry,_i:juniAddressPoolProfileIndex,_X:juniAddressPoolProfileRowStatus,_Y:juniAddressPoolProfileStart,_Z:juniAddressPoolProfileEnd,_a:juniAddressPoolProfileSize,_b:juniAddressPoolProfileInUse,'juniAddressAliasTable':juniAddressAliasTable,'juniAddressAliasEntry':juniAddressAliasEntry,_j:juniAddressAliasName,_l:juniAddressAliasRowStatus,_m:juniAddressAliasPoolName,'juniAddressSharedPoolTable':juniAddressSharedPoolTable,'juniAddressSharedPoolEntry':juniAddressSharedPoolEntry,_k:juniAddressSharedPoolIndex,_n:juniAddressSharedPoolRowStatus,_o:juniAddressSharedPoolName,_p:juniAddressSharedPoolDhcpPoolName,_q:juniAddressSharedPoolInUse,'juniAddressPoolTraps':juniAddressPoolTraps,'juniAddressPoolTrapPrefix':juniAddressPoolTrapPrefix,_r:juniAddressPoolHighAddrUtil,_s:juniAddressPoolAbatedAddrUtil,_t:juniAddressPoolNoAddresses,'juniAddressPoolMIBConformance':juniAddressPoolMIBConformance,'juniAddressPoolMIBCompliances':juniAddressPoolMIBCompliances,'juniAddressPoolCompliance':juniAddressPoolCompliance,'juniAddressPoolCompliance2':juniAddressPoolCompliance2,'juniAddressPoolCompliance3':juniAddressPoolCompliance3,'juniAddressPoolCompliance4':juniAddressPoolCompliance4,'juniAddressPoolCompliance5':juniAddressPoolCompliance5,'juniAddressPoolCompliance6':juniAddressPoolCompliance6,'juniAddressPoolMIBGroups':juniAddressPoolMIBGroups,_u:juniAddressPoolGroup,_v:juniAddressPoolGroup2,_M:juniAddressPoolTrapGroup,_g:juniAddressPoolGroup3,'juniAddressPoolDeprecatedGroup':juniAddressPoolDeprecatedGroup,_c:juniAddressAliasGroup,_w:juniAddressPoolGroup4,_x:juniAddressPoolGroup5})