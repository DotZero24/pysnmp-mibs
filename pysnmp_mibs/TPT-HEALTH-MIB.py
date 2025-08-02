_I='healthI2CIndex'
_H='healthVoltageIndex'
_G='healthFanIndex'
_F='healthTempIndex'
_E='not-accessible'
_D='TPT-HEALTH-MIB'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_tpa_objs,=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-objs')
tpt_health_objs=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,13))
if mibBuilder.loadTexts:tpt_health_objs.setRevisions(('2016-05-25 18:54',))
class HealthSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('normal',0),('info',1),('minor',2),('major',3),('critical',4)))
class HealthThresholdType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('minimum',1),('range',2),('maximum',3)))
_HealthTempTable_Object=MibTable
healthTempTable=_HealthTempTable_Object((1,3,6,1,4,1,10734,3,3,2,13,1))
if mibBuilder.loadTexts:healthTempTable.setStatus(_A)
_HealthTempEntry_Object=MibTableRow
healthTempEntry=_HealthTempEntry_Object((1,3,6,1,4,1,10734,3,3,2,13,1,1))
healthTempEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:healthTempEntry.setStatus(_A)
_HealthTempIndex_Type=Unsigned32
_HealthTempIndex_Object=MibTableColumn
healthTempIndex=_HealthTempIndex_Object((1,3,6,1,4,1,10734,3,3,2,13,1,1,1),_HealthTempIndex_Type())
healthTempIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:healthTempIndex.setStatus(_A)
class _HealthTempChannel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HealthTempChannel_Type.__name__=_C
_HealthTempChannel_Object=MibTableColumn
healthTempChannel=_HealthTempChannel_Object((1,3,6,1,4,1,10734,3,3,2,13,1,1,2),_HealthTempChannel_Type())
healthTempChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:healthTempChannel.setStatus(_A)
_HealthTempValue_Type=Unsigned32
_HealthTempValue_Object=MibTableColumn
healthTempValue=_HealthTempValue_Object((1,3,6,1,4,1,10734,3,3,2,13,1,1,3),_HealthTempValue_Type())
healthTempValue.setMaxAccess(_B)
if mibBuilder.loadTexts:healthTempValue.setStatus(_A)
_HealthTempSeverity_Type=HealthSeverity
_HealthTempSeverity_Object=MibTableColumn
healthTempSeverity=_HealthTempSeverity_Object((1,3,6,1,4,1,10734,3,3,2,13,1,1,4),_HealthTempSeverity_Type())
healthTempSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:healthTempSeverity.setStatus(_A)
_HealthTempThresholdType_Type=HealthThresholdType
_HealthTempThresholdType_Object=MibTableColumn
healthTempThresholdType=_HealthTempThresholdType_Object((1,3,6,1,4,1,10734,3,3,2,13,1,1,5),_HealthTempThresholdType_Type())
healthTempThresholdType.setMaxAccess(_B)
if mibBuilder.loadTexts:healthTempThresholdType.setStatus(_A)
_HealthTempMajor_Type=Unsigned32
_HealthTempMajor_Object=MibTableColumn
healthTempMajor=_HealthTempMajor_Object((1,3,6,1,4,1,10734,3,3,2,13,1,1,6),_HealthTempMajor_Type())
healthTempMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:healthTempMajor.setStatus(_A)
_HealthTempCritical_Type=Unsigned32
_HealthTempCritical_Object=MibTableColumn
healthTempCritical=_HealthTempCritical_Object((1,3,6,1,4,1,10734,3,3,2,13,1,1,7),_HealthTempCritical_Type())
healthTempCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:healthTempCritical.setStatus(_A)
_HealthFanTable_Object=MibTable
healthFanTable=_HealthFanTable_Object((1,3,6,1,4,1,10734,3,3,2,13,2))
if mibBuilder.loadTexts:healthFanTable.setStatus(_A)
_HealthFanEntry_Object=MibTableRow
healthFanEntry=_HealthFanEntry_Object((1,3,6,1,4,1,10734,3,3,2,13,2,1))
healthFanEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:healthFanEntry.setStatus(_A)
_HealthFanIndex_Type=Unsigned32
_HealthFanIndex_Object=MibTableColumn
healthFanIndex=_HealthFanIndex_Object((1,3,6,1,4,1,10734,3,3,2,13,2,1,1),_HealthFanIndex_Type())
healthFanIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:healthFanIndex.setStatus(_A)
class _HealthFanChannel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HealthFanChannel_Type.__name__=_C
_HealthFanChannel_Object=MibTableColumn
healthFanChannel=_HealthFanChannel_Object((1,3,6,1,4,1,10734,3,3,2,13,2,1,2),_HealthFanChannel_Type())
healthFanChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:healthFanChannel.setStatus(_A)
_HealthFanValue_Type=Unsigned32
_HealthFanValue_Object=MibTableColumn
healthFanValue=_HealthFanValue_Object((1,3,6,1,4,1,10734,3,3,2,13,2,1,3),_HealthFanValue_Type())
healthFanValue.setMaxAccess(_B)
if mibBuilder.loadTexts:healthFanValue.setStatus(_A)
_HealthFanSeverity_Type=HealthSeverity
_HealthFanSeverity_Object=MibTableColumn
healthFanSeverity=_HealthFanSeverity_Object((1,3,6,1,4,1,10734,3,3,2,13,2,1,4),_HealthFanSeverity_Type())
healthFanSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:healthFanSeverity.setStatus(_A)
_HealthFanThresholdType_Type=HealthThresholdType
_HealthFanThresholdType_Object=MibTableColumn
healthFanThresholdType=_HealthFanThresholdType_Object((1,3,6,1,4,1,10734,3,3,2,13,2,1,5),_HealthFanThresholdType_Type())
healthFanThresholdType.setMaxAccess(_B)
if mibBuilder.loadTexts:healthFanThresholdType.setStatus(_A)
_HealthFanMajor_Type=Unsigned32
_HealthFanMajor_Object=MibTableColumn
healthFanMajor=_HealthFanMajor_Object((1,3,6,1,4,1,10734,3,3,2,13,2,1,6),_HealthFanMajor_Type())
healthFanMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:healthFanMajor.setStatus(_A)
_HealthFanCritical_Type=Unsigned32
_HealthFanCritical_Object=MibTableColumn
healthFanCritical=_HealthFanCritical_Object((1,3,6,1,4,1,10734,3,3,2,13,2,1,7),_HealthFanCritical_Type())
healthFanCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:healthFanCritical.setStatus(_A)
_HealthVoltageTable_Object=MibTable
healthVoltageTable=_HealthVoltageTable_Object((1,3,6,1,4,1,10734,3,3,2,13,3))
if mibBuilder.loadTexts:healthVoltageTable.setStatus(_A)
_HealthVoltageEntry_Object=MibTableRow
healthVoltageEntry=_HealthVoltageEntry_Object((1,3,6,1,4,1,10734,3,3,2,13,3,1))
healthVoltageEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:healthVoltageEntry.setStatus(_A)
_HealthVoltageIndex_Type=Unsigned32
_HealthVoltageIndex_Object=MibTableColumn
healthVoltageIndex=_HealthVoltageIndex_Object((1,3,6,1,4,1,10734,3,3,2,13,3,1,1),_HealthVoltageIndex_Type())
healthVoltageIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:healthVoltageIndex.setStatus(_A)
class _HealthVoltageChannel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HealthVoltageChannel_Type.__name__=_C
_HealthVoltageChannel_Object=MibTableColumn
healthVoltageChannel=_HealthVoltageChannel_Object((1,3,6,1,4,1,10734,3,3,2,13,3,1,2),_HealthVoltageChannel_Type())
healthVoltageChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:healthVoltageChannel.setStatus(_A)
_HealthVoltageValue_Type=Unsigned32
_HealthVoltageValue_Object=MibTableColumn
healthVoltageValue=_HealthVoltageValue_Object((1,3,6,1,4,1,10734,3,3,2,13,3,1,3),_HealthVoltageValue_Type())
healthVoltageValue.setMaxAccess(_B)
if mibBuilder.loadTexts:healthVoltageValue.setStatus(_A)
_HealthVoltageSeverity_Type=HealthSeverity
_HealthVoltageSeverity_Object=MibTableColumn
healthVoltageSeverity=_HealthVoltageSeverity_Object((1,3,6,1,4,1,10734,3,3,2,13,3,1,4),_HealthVoltageSeverity_Type())
healthVoltageSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:healthVoltageSeverity.setStatus(_A)
_HealthVoltageThresholdType_Type=HealthThresholdType
_HealthVoltageThresholdType_Object=MibTableColumn
healthVoltageThresholdType=_HealthVoltageThresholdType_Object((1,3,6,1,4,1,10734,3,3,2,13,3,1,5),_HealthVoltageThresholdType_Type())
healthVoltageThresholdType.setMaxAccess(_B)
if mibBuilder.loadTexts:healthVoltageThresholdType.setStatus(_A)
_HealthVoltageMajor_Type=Unsigned32
_HealthVoltageMajor_Object=MibTableColumn
healthVoltageMajor=_HealthVoltageMajor_Object((1,3,6,1,4,1,10734,3,3,2,13,3,1,6),_HealthVoltageMajor_Type())
healthVoltageMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:healthVoltageMajor.setStatus(_A)
_HealthVoltageCritical_Type=Unsigned32
_HealthVoltageCritical_Object=MibTableColumn
healthVoltageCritical=_HealthVoltageCritical_Object((1,3,6,1,4,1,10734,3,3,2,13,3,1,7),_HealthVoltageCritical_Type())
healthVoltageCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:healthVoltageCritical.setStatus(_A)
_HealthVoltageNominal_Type=Unsigned32
_HealthVoltageNominal_Object=MibTableColumn
healthVoltageNominal=_HealthVoltageNominal_Object((1,3,6,1,4,1,10734,3,3,2,13,3,1,8),_HealthVoltageNominal_Type())
healthVoltageNominal.setMaxAccess(_B)
if mibBuilder.loadTexts:healthVoltageNominal.setStatus(_A)
_HealthI2CTable_Object=MibTable
healthI2CTable=_HealthI2CTable_Object((1,3,6,1,4,1,10734,3,3,2,13,4))
if mibBuilder.loadTexts:healthI2CTable.setStatus(_A)
_HealthI2CEntry_Object=MibTableRow
healthI2CEntry=_HealthI2CEntry_Object((1,3,6,1,4,1,10734,3,3,2,13,4,1))
healthI2CEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:healthI2CEntry.setStatus(_A)
_HealthI2CIndex_Type=Unsigned32
_HealthI2CIndex_Object=MibTableColumn
healthI2CIndex=_HealthI2CIndex_Object((1,3,6,1,4,1,10734,3,3,2,13,4,1,1),_HealthI2CIndex_Type())
healthI2CIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:healthI2CIndex.setStatus(_A)
class _HealthI2CChannel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HealthI2CChannel_Type.__name__=_C
_HealthI2CChannel_Object=MibTableColumn
healthI2CChannel=_HealthI2CChannel_Object((1,3,6,1,4,1,10734,3,3,2,13,4,1,2),_HealthI2CChannel_Type())
healthI2CChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:healthI2CChannel.setStatus(_A)
_HealthI2CValue_Type=Unsigned32
_HealthI2CValue_Object=MibTableColumn
healthI2CValue=_HealthI2CValue_Object((1,3,6,1,4,1,10734,3,3,2,13,4,1,3),_HealthI2CValue_Type())
healthI2CValue.setMaxAccess(_B)
if mibBuilder.loadTexts:healthI2CValue.setStatus(_A)
_HealthI2CSeverity_Type=HealthSeverity
_HealthI2CSeverity_Object=MibTableColumn
healthI2CSeverity=_HealthI2CSeverity_Object((1,3,6,1,4,1,10734,3,3,2,13,4,1,4),_HealthI2CSeverity_Type())
healthI2CSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:healthI2CSeverity.setStatus(_A)
_HealthI2CThresholdType_Type=HealthThresholdType
_HealthI2CThresholdType_Object=MibTableColumn
healthI2CThresholdType=_HealthI2CThresholdType_Object((1,3,6,1,4,1,10734,3,3,2,13,4,1,5),_HealthI2CThresholdType_Type())
healthI2CThresholdType.setMaxAccess(_B)
if mibBuilder.loadTexts:healthI2CThresholdType.setStatus(_A)
_HealthI2CMajor_Type=Unsigned32
_HealthI2CMajor_Object=MibTableColumn
healthI2CMajor=_HealthI2CMajor_Object((1,3,6,1,4,1,10734,3,3,2,13,4,1,6),_HealthI2CMajor_Type())
healthI2CMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:healthI2CMajor.setStatus(_A)
_HealthI2CCritical_Type=Unsigned32
_HealthI2CCritical_Object=MibTableColumn
healthI2CCritical=_HealthI2CCritical_Object((1,3,6,1,4,1,10734,3,3,2,13,4,1,7),_HealthI2CCritical_Type())
healthI2CCritical.setMaxAccess(_B)
if mibBuilder.loadTexts:healthI2CCritical.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'HealthSeverity':HealthSeverity,'HealthThresholdType':HealthThresholdType,'tpt-health-objs':tpt_health_objs,'healthTempTable':healthTempTable,'healthTempEntry':healthTempEntry,_F:healthTempIndex,'healthTempChannel':healthTempChannel,'healthTempValue':healthTempValue,'healthTempSeverity':healthTempSeverity,'healthTempThresholdType':healthTempThresholdType,'healthTempMajor':healthTempMajor,'healthTempCritical':healthTempCritical,'healthFanTable':healthFanTable,'healthFanEntry':healthFanEntry,_G:healthFanIndex,'healthFanChannel':healthFanChannel,'healthFanValue':healthFanValue,'healthFanSeverity':healthFanSeverity,'healthFanThresholdType':healthFanThresholdType,'healthFanMajor':healthFanMajor,'healthFanCritical':healthFanCritical,'healthVoltageTable':healthVoltageTable,'healthVoltageEntry':healthVoltageEntry,_H:healthVoltageIndex,'healthVoltageChannel':healthVoltageChannel,'healthVoltageValue':healthVoltageValue,'healthVoltageSeverity':healthVoltageSeverity,'healthVoltageThresholdType':healthVoltageThresholdType,'healthVoltageMajor':healthVoltageMajor,'healthVoltageCritical':healthVoltageCritical,'healthVoltageNominal':healthVoltageNominal,'healthI2CTable':healthI2CTable,'healthI2CEntry':healthI2CEntry,_I:healthI2CIndex,'healthI2CChannel':healthI2CChannel,'healthI2CValue':healthI2CValue,'healthI2CSeverity':healthI2CSeverity,'healthI2CThresholdType':healthI2CThresholdType,'healthI2CMajor':healthI2CMajor,'healthI2CCritical':healthI2CCritical})