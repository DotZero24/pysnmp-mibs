_q='lldpXPnoMRPGroup'
_p='lldpXPnoRemGroup'
_o='lldpXPnoLocGroup'
_n='lldpXPnoConfigGroup'
_m='lldpXPnoRemPortMrrtStatus'
_l='lldpXPnoRemPortMrpUuId'
_k='lldpXPnoLocPortMrrtStatus'
_j='lldpXPnoLocPortMrpUuId'
_i='lldpXPnoConfigMrpTxEnable'
_h='lldpXPnoRemPortNoS'
_g='lldpXPnoRemPortStatusRT3'
_f='lldpXPnoRemPortStatusRT2'
_e='lldpXPnoRemPortRxDValue'
_d='lldpXPnoRemPortTxDValue'
_c='lldpXPnoRemLPDValue'
_b='lldpXPnoLocPortNoS'
_a='lldpXPnoLocPortStatusRT3'
_Z='lldpXPnoLocPortStatusRT2'
_Y='lldpXPnoLocPortRxDValue'
_X='lldpXPnoLocPortTxDValue'
_W='lldpXPnoLocLPDValue'
_V='lldpXPnoConfigAliasTxEnable'
_U='lldpXPnoConfigPortStatusTxEnable'
_T='lldpXPnoConfigSPDTxEnable'
_S='lldpXPnoConfigEntry'
_R='lldpRemTimeMark'
_Q='lldpRemLocalPortNum'
_P='lldpRemIndex'
_O='lldpLocPortNum'
_N='OctetString'
_M='up'
_L='running'
_K='read-write'
_J='Unsigned32'
_I='TruthValue'
_H='LLDP-MIB'
_G='configured'
_F='off'
_E='ns'
_D='Integer32'
_C='read-only'
_B='LLDP-EXT-PNO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lldpExtensions,lldpLocPortNum,lldpPortConfigEntry,lldpRemIndex,lldpRemLocalPortNum,lldpRemTimeMark=mibBuilder.importSymbols(_H,'lldpExtensions',_O,'lldpPortConfigEntry',_P,_Q,_R)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
lldpXPnoMIB=ModuleIdentity((1,0,8802,1,1,2,1,5,3791))
if mibBuilder.loadTexts:lldpXPnoMIB.setRevisions(('2006-03-09 00:00','2006-02-28 00:00','2005-08-31 00:00','2005-05-30 00:00'))
_LldpXPnoObjects_ObjectIdentity=ObjectIdentity
lldpXPnoObjects=_LldpXPnoObjects_ObjectIdentity((1,0,8802,1,1,2,1,5,3791,1))
_LldpXPnoConfig_ObjectIdentity=ObjectIdentity
lldpXPnoConfig=_LldpXPnoConfig_ObjectIdentity((1,0,8802,1,1,2,1,5,3791,1,1))
_LldpXPnoConfigTable_Object=MibTable
lldpXPnoConfigTable=_LldpXPnoConfigTable_Object((1,0,8802,1,1,2,1,5,3791,1,1,1))
if mibBuilder.loadTexts:lldpXPnoConfigTable.setStatus(_A)
_LldpXPnoConfigEntry_Object=MibTableRow
lldpXPnoConfigEntry=_LldpXPnoConfigEntry_Object((1,0,8802,1,1,2,1,5,3791,1,1,1,1))
if mibBuilder.loadTexts:lldpXPnoConfigEntry.setStatus(_A)
class _LldpXPnoConfigSPDTxEnable_Type(TruthValue):defaultValue=1
_LldpXPnoConfigSPDTxEnable_Type.__name__=_I
_LldpXPnoConfigSPDTxEnable_Object=MibTableColumn
lldpXPnoConfigSPDTxEnable=_LldpXPnoConfigSPDTxEnable_Object((1,0,8802,1,1,2,1,5,3791,1,1,1,1,1),_LldpXPnoConfigSPDTxEnable_Type())
lldpXPnoConfigSPDTxEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:lldpXPnoConfigSPDTxEnable.setStatus(_A)
class _LldpXPnoConfigPortStatusTxEnable_Type(TruthValue):defaultValue=1
_LldpXPnoConfigPortStatusTxEnable_Type.__name__=_I
_LldpXPnoConfigPortStatusTxEnable_Object=MibTableColumn
lldpXPnoConfigPortStatusTxEnable=_LldpXPnoConfigPortStatusTxEnable_Object((1,0,8802,1,1,2,1,5,3791,1,1,1,1,2),_LldpXPnoConfigPortStatusTxEnable_Type())
lldpXPnoConfigPortStatusTxEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:lldpXPnoConfigPortStatusTxEnable.setStatus(_A)
class _LldpXPnoConfigAliasTxEnable_Type(TruthValue):defaultValue=2
_LldpXPnoConfigAliasTxEnable_Type.__name__=_I
_LldpXPnoConfigAliasTxEnable_Object=MibTableColumn
lldpXPnoConfigAliasTxEnable=_LldpXPnoConfigAliasTxEnable_Object((1,0,8802,1,1,2,1,5,3791,1,1,1,1,3),_LldpXPnoConfigAliasTxEnable_Type())
lldpXPnoConfigAliasTxEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:lldpXPnoConfigAliasTxEnable.setStatus(_A)
class _LldpXPnoConfigMrpTxEnable_Type(TruthValue):defaultValue=1
_LldpXPnoConfigMrpTxEnable_Type.__name__=_I
_LldpXPnoConfigMrpTxEnable_Object=MibTableColumn
lldpXPnoConfigMrpTxEnable=_LldpXPnoConfigMrpTxEnable_Object((1,0,8802,1,1,2,1,5,3791,1,1,1,1,4),_LldpXPnoConfigMrpTxEnable_Type())
lldpXPnoConfigMrpTxEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:lldpXPnoConfigMrpTxEnable.setStatus(_A)
_LldpXPnoLocalData_ObjectIdentity=ObjectIdentity
lldpXPnoLocalData=_LldpXPnoLocalData_ObjectIdentity((1,0,8802,1,1,2,1,5,3791,1,2))
_LldpXPnoLocTable_Object=MibTable
lldpXPnoLocTable=_LldpXPnoLocTable_Object((1,0,8802,1,1,2,1,5,3791,1,2,1))
if mibBuilder.loadTexts:lldpXPnoLocTable.setStatus(_A)
_LldpXPnoLocEntry_Object=MibTableRow
lldpXPnoLocEntry=_LldpXPnoLocEntry_Object((1,0,8802,1,1,2,1,5,3791,1,2,1,1))
lldpXPnoLocEntry.setIndexNames((0,_H,_O))
if mibBuilder.loadTexts:lldpXPnoLocEntry.setStatus(_A)
class _LldpXPnoLocLPDValue_Type(Unsigned32):defaultValue=0
_LldpXPnoLocLPDValue_Type.__name__=_J
_LldpXPnoLocLPDValue_Object=MibTableColumn
lldpXPnoLocLPDValue=_LldpXPnoLocLPDValue_Object((1,0,8802,1,1,2,1,5,3791,1,2,1,1,1),_LldpXPnoLocLPDValue_Type())
lldpXPnoLocLPDValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoLocLPDValue.setStatus(_A)
if mibBuilder.loadTexts:lldpXPnoLocLPDValue.setUnits(_E)
class _LldpXPnoLocPortTxDValue_Type(Unsigned32):defaultValue=0
_LldpXPnoLocPortTxDValue_Type.__name__=_J
_LldpXPnoLocPortTxDValue_Object=MibTableColumn
lldpXPnoLocPortTxDValue=_LldpXPnoLocPortTxDValue_Object((1,0,8802,1,1,2,1,5,3791,1,2,1,1,2),_LldpXPnoLocPortTxDValue_Type())
lldpXPnoLocPortTxDValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoLocPortTxDValue.setStatus(_A)
if mibBuilder.loadTexts:lldpXPnoLocPortTxDValue.setUnits(_E)
class _LldpXPnoLocPortRxDValue_Type(Unsigned32):defaultValue=0
_LldpXPnoLocPortRxDValue_Type.__name__=_J
_LldpXPnoLocPortRxDValue_Object=MibTableColumn
lldpXPnoLocPortRxDValue=_LldpXPnoLocPortRxDValue_Object((1,0,8802,1,1,2,1,5,3791,1,2,1,1,3),_LldpXPnoLocPortRxDValue_Type())
lldpXPnoLocPortRxDValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoLocPortRxDValue.setStatus(_A)
if mibBuilder.loadTexts:lldpXPnoLocPortRxDValue.setUnits(_E)
class _LldpXPnoLocPortStatusRT2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_G,1),(_L,2)))
_LldpXPnoLocPortStatusRT2_Type.__name__=_D
_LldpXPnoLocPortStatusRT2_Object=MibTableColumn
lldpXPnoLocPortStatusRT2=_LldpXPnoLocPortStatusRT2_Object((1,0,8802,1,1,2,1,5,3791,1,2,1,1,4),_LldpXPnoLocPortStatusRT2_Type())
lldpXPnoLocPortStatusRT2.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoLocPortStatusRT2.setStatus(_A)
class _LldpXPnoLocPortStatusRT3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),(_G,1),(_M,2),('down',3),(_L,4)))
_LldpXPnoLocPortStatusRT3_Type.__name__=_D
_LldpXPnoLocPortStatusRT3_Object=MibTableColumn
lldpXPnoLocPortStatusRT3=_LldpXPnoLocPortStatusRT3_Object((1,0,8802,1,1,2,1,5,3791,1,2,1,1,5),_LldpXPnoLocPortStatusRT3_Type())
lldpXPnoLocPortStatusRT3.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoLocPortStatusRT3.setStatus(_A)
_LldpXPnoLocPortNoS_Type=DisplayString
_LldpXPnoLocPortNoS_Object=MibTableColumn
lldpXPnoLocPortNoS=_LldpXPnoLocPortNoS_Object((1,0,8802,1,1,2,1,5,3791,1,2,1,1,6),_LldpXPnoLocPortNoS_Type())
lldpXPnoLocPortNoS.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoLocPortNoS.setStatus(_A)
class _LldpXPnoLocPortMrpUuId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_LldpXPnoLocPortMrpUuId_Type.__name__=_N
_LldpXPnoLocPortMrpUuId_Object=MibTableColumn
lldpXPnoLocPortMrpUuId=_LldpXPnoLocPortMrpUuId_Object((1,0,8802,1,1,2,1,5,3791,1,2,1,1,7),_LldpXPnoLocPortMrpUuId_Type())
lldpXPnoLocPortMrpUuId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoLocPortMrpUuId.setStatus(_A)
class _LldpXPnoLocPortMrrtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_G,1),(_M,2)))
_LldpXPnoLocPortMrrtStatus_Type.__name__=_D
_LldpXPnoLocPortMrrtStatus_Object=MibTableColumn
lldpXPnoLocPortMrrtStatus=_LldpXPnoLocPortMrrtStatus_Object((1,0,8802,1,1,2,1,5,3791,1,2,1,1,8),_LldpXPnoLocPortMrrtStatus_Type())
lldpXPnoLocPortMrrtStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoLocPortMrrtStatus.setStatus(_A)
_LldpXPnoRemoteData_ObjectIdentity=ObjectIdentity
lldpXPnoRemoteData=_LldpXPnoRemoteData_ObjectIdentity((1,0,8802,1,1,2,1,5,3791,1,3))
_LldpXPnoRemTable_Object=MibTable
lldpXPnoRemTable=_LldpXPnoRemTable_Object((1,0,8802,1,1,2,1,5,3791,1,3,1))
if mibBuilder.loadTexts:lldpXPnoRemTable.setStatus(_A)
_LldpXPnoRemEntry_Object=MibTableRow
lldpXPnoRemEntry=_LldpXPnoRemEntry_Object((1,0,8802,1,1,2,1,5,3791,1,3,1,1))
lldpXPnoRemEntry.setIndexNames((0,_H,_R),(0,_H,_Q),(0,_H,_P))
if mibBuilder.loadTexts:lldpXPnoRemEntry.setStatus(_A)
_LldpXPnoRemLPDValue_Type=Unsigned32
_LldpXPnoRemLPDValue_Object=MibTableColumn
lldpXPnoRemLPDValue=_LldpXPnoRemLPDValue_Object((1,0,8802,1,1,2,1,5,3791,1,3,1,1,1),_LldpXPnoRemLPDValue_Type())
lldpXPnoRemLPDValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoRemLPDValue.setStatus(_A)
if mibBuilder.loadTexts:lldpXPnoRemLPDValue.setUnits(_E)
_LldpXPnoRemPortTxDValue_Type=Unsigned32
_LldpXPnoRemPortTxDValue_Object=MibTableColumn
lldpXPnoRemPortTxDValue=_LldpXPnoRemPortTxDValue_Object((1,0,8802,1,1,2,1,5,3791,1,3,1,1,2),_LldpXPnoRemPortTxDValue_Type())
lldpXPnoRemPortTxDValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoRemPortTxDValue.setStatus(_A)
if mibBuilder.loadTexts:lldpXPnoRemPortTxDValue.setUnits(_E)
_LldpXPnoRemPortRxDValue_Type=Unsigned32
_LldpXPnoRemPortRxDValue_Object=MibTableColumn
lldpXPnoRemPortRxDValue=_LldpXPnoRemPortRxDValue_Object((1,0,8802,1,1,2,1,5,3791,1,3,1,1,3),_LldpXPnoRemPortRxDValue_Type())
lldpXPnoRemPortRxDValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoRemPortRxDValue.setStatus(_A)
if mibBuilder.loadTexts:lldpXPnoRemPortRxDValue.setUnits(_E)
class _LldpXPnoRemPortStatusRT2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_G,1),(_L,2)))
_LldpXPnoRemPortStatusRT2_Type.__name__=_D
_LldpXPnoRemPortStatusRT2_Object=MibTableColumn
lldpXPnoRemPortStatusRT2=_LldpXPnoRemPortStatusRT2_Object((1,0,8802,1,1,2,1,5,3791,1,3,1,1,4),_LldpXPnoRemPortStatusRT2_Type())
lldpXPnoRemPortStatusRT2.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoRemPortStatusRT2.setStatus(_A)
class _LldpXPnoRemPortStatusRT3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),(_G,1),(_M,2),('down',3),(_L,4)))
_LldpXPnoRemPortStatusRT3_Type.__name__=_D
_LldpXPnoRemPortStatusRT3_Object=MibTableColumn
lldpXPnoRemPortStatusRT3=_LldpXPnoRemPortStatusRT3_Object((1,0,8802,1,1,2,1,5,3791,1,3,1,1,5),_LldpXPnoRemPortStatusRT3_Type())
lldpXPnoRemPortStatusRT3.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoRemPortStatusRT3.setStatus(_A)
_LldpXPnoRemPortNoS_Type=DisplayString
_LldpXPnoRemPortNoS_Object=MibTableColumn
lldpXPnoRemPortNoS=_LldpXPnoRemPortNoS_Object((1,0,8802,1,1,2,1,5,3791,1,3,1,1,6),_LldpXPnoRemPortNoS_Type())
lldpXPnoRemPortNoS.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoRemPortNoS.setStatus(_A)
class _LldpXPnoRemPortMrpUuId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_LldpXPnoRemPortMrpUuId_Type.__name__=_N
_LldpXPnoRemPortMrpUuId_Object=MibTableColumn
lldpXPnoRemPortMrpUuId=_LldpXPnoRemPortMrpUuId_Object((1,0,8802,1,1,2,1,5,3791,1,3,1,1,7),_LldpXPnoRemPortMrpUuId_Type())
lldpXPnoRemPortMrpUuId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoRemPortMrpUuId.setStatus(_A)
class _LldpXPnoRemPortMrrtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_G,1),(_M,2)))
_LldpXPnoRemPortMrrtStatus_Type.__name__=_D
_LldpXPnoRemPortMrrtStatus_Object=MibTableColumn
lldpXPnoRemPortMrrtStatus=_LldpXPnoRemPortMrrtStatus_Object((1,0,8802,1,1,2,1,5,3791,1,3,1,1,8),_LldpXPnoRemPortMrrtStatus_Type())
lldpXPnoRemPortMrrtStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXPnoRemPortMrrtStatus.setStatus(_A)
_LldpXPnoConformance_ObjectIdentity=ObjectIdentity
lldpXPnoConformance=_LldpXPnoConformance_ObjectIdentity((1,0,8802,1,1,2,1,5,3791,2))
_LldpXPnoCompliances_ObjectIdentity=ObjectIdentity
lldpXPnoCompliances=_LldpXPnoCompliances_ObjectIdentity((1,0,8802,1,1,2,1,5,3791,2,1))
_LldpXPnoGroups_ObjectIdentity=ObjectIdentity
lldpXPnoGroups=_LldpXPnoGroups_ObjectIdentity((1,0,8802,1,1,2,1,5,3791,2,2))
lldpPortConfigEntry.registerAugmentions((_B,_S))
lldpXPnoConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpXPnoConfigGroup=ObjectGroup((1,0,8802,1,1,2,1,5,3791,2,2,1))
lldpXPnoConfigGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:lldpXPnoConfigGroup.setStatus(_A)
lldpXPnoLocGroup=ObjectGroup((1,0,8802,1,1,2,1,5,3791,2,2,2))
lldpXPnoLocGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:lldpXPnoLocGroup.setStatus(_A)
lldpXPnoRemGroup=ObjectGroup((1,0,8802,1,1,2,1,5,3791,2,2,3))
lldpXPnoRemGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:lldpXPnoRemGroup.setStatus(_A)
lldpXPnoMRPGroup=ObjectGroup((1,0,8802,1,1,2,1,5,3791,2,2,4))
lldpXPnoMRPGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:lldpXPnoMRPGroup.setStatus(_A)
lldpXPnoCompliance=ModuleCompliance((1,0,8802,1,1,2,1,5,3791,2,1,1))
lldpXPnoCompliance.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:lldpXPnoCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lldpXPnoMIB':lldpXPnoMIB,'lldpXPnoObjects':lldpXPnoObjects,'lldpXPnoConfig':lldpXPnoConfig,'lldpXPnoConfigTable':lldpXPnoConfigTable,_S:lldpXPnoConfigEntry,_T:lldpXPnoConfigSPDTxEnable,_U:lldpXPnoConfigPortStatusTxEnable,_V:lldpXPnoConfigAliasTxEnable,_i:lldpXPnoConfigMrpTxEnable,'lldpXPnoLocalData':lldpXPnoLocalData,'lldpXPnoLocTable':lldpXPnoLocTable,'lldpXPnoLocEntry':lldpXPnoLocEntry,_W:lldpXPnoLocLPDValue,_X:lldpXPnoLocPortTxDValue,_Y:lldpXPnoLocPortRxDValue,_Z:lldpXPnoLocPortStatusRT2,_a:lldpXPnoLocPortStatusRT3,_b:lldpXPnoLocPortNoS,_j:lldpXPnoLocPortMrpUuId,_k:lldpXPnoLocPortMrrtStatus,'lldpXPnoRemoteData':lldpXPnoRemoteData,'lldpXPnoRemTable':lldpXPnoRemTable,'lldpXPnoRemEntry':lldpXPnoRemEntry,_c:lldpXPnoRemLPDValue,_d:lldpXPnoRemPortTxDValue,_e:lldpXPnoRemPortRxDValue,_f:lldpXPnoRemPortStatusRT2,_g:lldpXPnoRemPortStatusRT3,_h:lldpXPnoRemPortNoS,_l:lldpXPnoRemPortMrpUuId,_m:lldpXPnoRemPortMrrtStatus,'lldpXPnoConformance':lldpXPnoConformance,'lldpXPnoCompliances':lldpXPnoCompliances,'lldpXPnoCompliance':lldpXPnoCompliance,'lldpXPnoGroups':lldpXPnoGroups,_n:lldpXPnoConfigGroup,_o:lldpXPnoLocGroup,_p:lldpXPnoRemGroup,_q:lldpXPnoMRPGroup})