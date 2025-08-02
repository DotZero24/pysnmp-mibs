_R='vsiGroup'
_Q='vsiMacLimitNotifyVsi'
_P='vsiMacLimitActionVsi'
_O='vsiMacLimitVsi'
_N='vsiVlanLearningMode'
_M='vsiVlanLearning'
_L='vsiCreationType'
_K='vsiServiceId'
_J='vsiMTUSize'
_I='vsiType'
_H='disabled'
_G='enabled'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-write'
_B='INFINERA-TP-PXMVSI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnVlanLearningMode,InfnVsiCreationType,InfnVsiMacLimitAction,InfnVsiType=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnVlanLearningMode','InfnVsiCreationType','InfnVsiMacLimitAction','InfnVsiType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vsiMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,70))
_VsiTable_Object=MibTable
vsiTable=_VsiTable_Object((1,3,6,1,4,1,21296,2,2,2,2,70,1))
if mibBuilder.loadTexts:vsiTable.setStatus(_A)
_VsiEntry_Object=MibTableRow
vsiEntry=_VsiEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,70,1,1))
vsiEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:vsiEntry.setStatus(_A)
_VsiType_Type=InfnVsiType
_VsiType_Object=MibTableColumn
vsiType=_VsiType_Object((1,3,6,1,4,1,21296,2,2,2,2,70,1,1,1),_VsiType_Type())
vsiType.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiType.setStatus(_A)
_VsiMTUSize_Type=Integer32
_VsiMTUSize_Object=MibTableColumn
vsiMTUSize=_VsiMTUSize_Object((1,3,6,1,4,1,21296,2,2,2,2,70,1,1,2),_VsiMTUSize_Type())
vsiMTUSize.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiMTUSize.setStatus(_A)
_VsiServiceId_Type=DisplayString
_VsiServiceId_Object=MibTableColumn
vsiServiceId=_VsiServiceId_Object((1,3,6,1,4,1,21296,2,2,2,2,70,1,1,3),_VsiServiceId_Type())
vsiServiceId.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiServiceId.setStatus(_A)
_VsiCreationType_Type=InfnVsiCreationType
_VsiCreationType_Object=MibTableColumn
vsiCreationType=_VsiCreationType_Object((1,3,6,1,4,1,21296,2,2,2,2,70,1,1,4),_VsiCreationType_Type())
vsiCreationType.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiCreationType.setStatus(_A)
class _VsiVlanLearning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_VsiVlanLearning_Type.__name__=_D
_VsiVlanLearning_Object=MibTableColumn
vsiVlanLearning=_VsiVlanLearning_Object((1,3,6,1,4,1,21296,2,2,2,2,70,1,1,5),_VsiVlanLearning_Type())
vsiVlanLearning.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiVlanLearning.setStatus(_A)
_VsiVlanLearningMode_Type=InfnVlanLearningMode
_VsiVlanLearningMode_Object=MibTableColumn
vsiVlanLearningMode=_VsiVlanLearningMode_Object((1,3,6,1,4,1,21296,2,2,2,2,70,1,1,6),_VsiVlanLearningMode_Type())
vsiVlanLearningMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiVlanLearningMode.setStatus(_A)
_VsiMacLimitVsi_Type=Integer32
_VsiMacLimitVsi_Object=MibTableColumn
vsiMacLimitVsi=_VsiMacLimitVsi_Object((1,3,6,1,4,1,21296,2,2,2,2,70,1,1,7),_VsiMacLimitVsi_Type())
vsiMacLimitVsi.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiMacLimitVsi.setStatus(_A)
_VsiMacLimitActionVsi_Type=InfnVsiMacLimitAction
_VsiMacLimitActionVsi_Object=MibTableColumn
vsiMacLimitActionVsi=_VsiMacLimitActionVsi_Object((1,3,6,1,4,1,21296,2,2,2,2,70,1,1,8),_VsiMacLimitActionVsi_Type())
vsiMacLimitActionVsi.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiMacLimitActionVsi.setStatus(_A)
class _VsiMacLimitNotifyVsi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_VsiMacLimitNotifyVsi_Type.__name__=_D
_VsiMacLimitNotifyVsi_Object=MibTableColumn
vsiMacLimitNotifyVsi=_VsiMacLimitNotifyVsi_Object((1,3,6,1,4,1,21296,2,2,2,2,70,1,1,9),_VsiMacLimitNotifyVsi_Type())
vsiMacLimitNotifyVsi.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiMacLimitNotifyVsi.setStatus(_A)
_VsiConformance_ObjectIdentity=ObjectIdentity
vsiConformance=_VsiConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,70,3))
_VsiCompliances_ObjectIdentity=ObjectIdentity
vsiCompliances=_VsiCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,70,3,1))
_VsiGroups_ObjectIdentity=ObjectIdentity
vsiGroups=_VsiGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,70,3,2))
vsiGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,70,3,2,1))
vsiGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:vsiGroup.setStatus(_A)
vsiCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,70,3,1,1))
vsiCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:vsiCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vsiMIB':vsiMIB,'vsiTable':vsiTable,'vsiEntry':vsiEntry,_I:vsiType,_J:vsiMTUSize,_K:vsiServiceId,_L:vsiCreationType,_M:vsiVlanLearning,_N:vsiVlanLearningMode,_O:vsiMacLimitVsi,_P:vsiMacLimitActionVsi,_Q:vsiMacLimitNotifyVsi,'vsiConformance':vsiConformance,'vsiCompliances':vsiCompliances,'vsiCompliance':vsiCompliance,'vsiGroups':vsiGroups,_R:vsiGroup})