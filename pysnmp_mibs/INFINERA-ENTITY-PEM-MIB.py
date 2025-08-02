_O='pemGroup'
_N='inputVoltage'
_M='transientVoltageThreshold'
_L='overVoltageThreshold'
_K='underVoltageThreshold'
_J='installedRatingAmps'
_I='provRatingAmps'
_H='pemProvEqptType'
_G='pemMoId'
_F='read-create'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='INFINERA-ENTITY-PEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatTenths,InfnEqptType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pemMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,15))
_PemTable_Object=MibTable
pemTable=_PemTable_Object((1,3,6,1,4,1,21296,2,2,2,1,15,1))
if mibBuilder.loadTexts:pemTable.setStatus(_A)
_PemEntry_Object=MibTableRow
pemEntry=_PemEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,15,1,1))
pemEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pemEntry.setStatus(_A)
_PemMoId_Type=DisplayString
_PemMoId_Object=MibTableColumn
pemMoId=_PemMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,15,1,1,1),_PemMoId_Type())
pemMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:pemMoId.setStatus(_A)
_PemProvEqptType_Type=InfnEqptType
_PemProvEqptType_Object=MibTableColumn
pemProvEqptType=_PemProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,15,1,1,2),_PemProvEqptType_Type())
pemProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:pemProvEqptType.setStatus(_A)
_ProvRatingAmps_Type=Unsigned32
_ProvRatingAmps_Object=MibTableColumn
provRatingAmps=_ProvRatingAmps_Object((1,3,6,1,4,1,21296,2,2,2,1,15,1,1,3),_ProvRatingAmps_Type())
provRatingAmps.setMaxAccess(_F)
if mibBuilder.loadTexts:provRatingAmps.setStatus(_A)
_InstalledRatingAmps_Type=Unsigned32
_InstalledRatingAmps_Object=MibTableColumn
installedRatingAmps=_InstalledRatingAmps_Object((1,3,6,1,4,1,21296,2,2,2,1,15,1,1,4),_InstalledRatingAmps_Type())
installedRatingAmps.setMaxAccess(_C)
if mibBuilder.loadTexts:installedRatingAmps.setStatus(_A)
_UnderVoltageThreshold_Type=FloatTenths
_UnderVoltageThreshold_Object=MibTableColumn
underVoltageThreshold=_UnderVoltageThreshold_Object((1,3,6,1,4,1,21296,2,2,2,1,15,1,1,5),_UnderVoltageThreshold_Type())
underVoltageThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:underVoltageThreshold.setStatus(_A)
_OverVoltageThreshold_Type=FloatTenths
_OverVoltageThreshold_Object=MibTableColumn
overVoltageThreshold=_OverVoltageThreshold_Object((1,3,6,1,4,1,21296,2,2,2,1,15,1,1,6),_OverVoltageThreshold_Type())
overVoltageThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:overVoltageThreshold.setStatus(_A)
_TransientVoltageThreshold_Type=FloatTenths
_TransientVoltageThreshold_Object=MibTableColumn
transientVoltageThreshold=_TransientVoltageThreshold_Object((1,3,6,1,4,1,21296,2,2,2,1,15,1,1,7),_TransientVoltageThreshold_Type())
transientVoltageThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:transientVoltageThreshold.setStatus(_A)
_InputVoltage_Type=Integer32
_InputVoltage_Object=MibTableColumn
inputVoltage=_InputVoltage_Object((1,3,6,1,4,1,21296,2,2,2,1,15,1,1,8),_InputVoltage_Type())
inputVoltage.setMaxAccess(_F)
if mibBuilder.loadTexts:inputVoltage.setStatus(_A)
_PemConformance_ObjectIdentity=ObjectIdentity
pemConformance=_PemConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,15,3))
_PemCompliances_ObjectIdentity=ObjectIdentity
pemCompliances=_PemCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,15,3,1))
_PemGroups_ObjectIdentity=ObjectIdentity
pemGroups=_PemGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,15,3,2))
pemGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,15,3,2,1))
pemGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:pemGroup.setStatus(_A)
pemCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,15,3,1,1))
pemCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:pemCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pemMIB':pemMIB,'pemTable':pemTable,'pemEntry':pemEntry,_G:pemMoId,_H:pemProvEqptType,_I:provRatingAmps,_J:installedRatingAmps,_K:underVoltageThreshold,_L:overVoltageThreshold,_M:transientVoltageThreshold,_N:inputVoltage,'pemConformance':pemConformance,'pemCompliances':pemCompliances,'pemCompliance':pemCompliance,'pemGroups':pemGroups,_O:pemGroup})