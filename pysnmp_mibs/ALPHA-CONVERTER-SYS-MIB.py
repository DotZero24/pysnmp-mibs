_M='converterGroup'
_L='convSysSystemNumber'
_K='convSysTotalLoadCurrent'
_J='convSysSystemVoltage'
_I='convSysAverageConverterInputVoltage'
_H='convSysAverageConverterOutputVoltage'
_G='convSysTotalCapacityInstalledPower'
_F='convSysTotalCapacityInstalledAmps'
_E='convSysTotalOutputPower'
_D='convSysTotalOutputCurrent'
_C='read-only'
_B='ALPHA-CONVERTER-SYS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ScaledNumber,simple=mibBuilder.importSymbols('ALPHA-RESOURCE-MIB','ScaledNumber','simple')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
converterSystem=ModuleIdentity((1,3,6,1,4,1,7309,5,3,2))
if mibBuilder.loadTexts:converterSystem.setRevisions(('2015-07-28 00:00','2015-07-23 00:00','2015-06-23 00:00'))
_ConvSysTotalOutputCurrent_Type=ScaledNumber
_ConvSysTotalOutputCurrent_Object=MibScalar
convSysTotalOutputCurrent=_ConvSysTotalOutputCurrent_Object((1,3,6,1,4,1,7309,5,3,2,1),_ConvSysTotalOutputCurrent_Type())
convSysTotalOutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:convSysTotalOutputCurrent.setStatus(_A)
_ConvSysTotalOutputPower_Type=ScaledNumber
_ConvSysTotalOutputPower_Object=MibScalar
convSysTotalOutputPower=_ConvSysTotalOutputPower_Object((1,3,6,1,4,1,7309,5,3,2,2),_ConvSysTotalOutputPower_Type())
convSysTotalOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:convSysTotalOutputPower.setStatus(_A)
_ConvSysTotalCapacityInstalledAmps_Type=ScaledNumber
_ConvSysTotalCapacityInstalledAmps_Object=MibScalar
convSysTotalCapacityInstalledAmps=_ConvSysTotalCapacityInstalledAmps_Object((1,3,6,1,4,1,7309,5,3,2,3),_ConvSysTotalCapacityInstalledAmps_Type())
convSysTotalCapacityInstalledAmps.setMaxAccess(_C)
if mibBuilder.loadTexts:convSysTotalCapacityInstalledAmps.setStatus(_A)
_ConvSysTotalCapacityInstalledPower_Type=ScaledNumber
_ConvSysTotalCapacityInstalledPower_Object=MibScalar
convSysTotalCapacityInstalledPower=_ConvSysTotalCapacityInstalledPower_Object((1,3,6,1,4,1,7309,5,3,2,4),_ConvSysTotalCapacityInstalledPower_Type())
convSysTotalCapacityInstalledPower.setMaxAccess(_C)
if mibBuilder.loadTexts:convSysTotalCapacityInstalledPower.setStatus(_A)
_ConvSysAverageConverterOutputVoltage_Type=ScaledNumber
_ConvSysAverageConverterOutputVoltage_Object=MibScalar
convSysAverageConverterOutputVoltage=_ConvSysAverageConverterOutputVoltage_Object((1,3,6,1,4,1,7309,5,3,2,5),_ConvSysAverageConverterOutputVoltage_Type())
convSysAverageConverterOutputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:convSysAverageConverterOutputVoltage.setStatus(_A)
_ConvSysAverageConverterInputVoltage_Type=ScaledNumber
_ConvSysAverageConverterInputVoltage_Object=MibScalar
convSysAverageConverterInputVoltage=_ConvSysAverageConverterInputVoltage_Object((1,3,6,1,4,1,7309,5,3,2,6),_ConvSysAverageConverterInputVoltage_Type())
convSysAverageConverterInputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:convSysAverageConverterInputVoltage.setStatus(_A)
_ConvSysSystemVoltage_Type=ScaledNumber
_ConvSysSystemVoltage_Object=MibScalar
convSysSystemVoltage=_ConvSysSystemVoltage_Object((1,3,6,1,4,1,7309,5,3,2,7),_ConvSysSystemVoltage_Type())
convSysSystemVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:convSysSystemVoltage.setStatus(_A)
_ConvSysTotalLoadCurrent_Type=ScaledNumber
_ConvSysTotalLoadCurrent_Object=MibScalar
convSysTotalLoadCurrent=_ConvSysTotalLoadCurrent_Object((1,3,6,1,4,1,7309,5,3,2,8),_ConvSysTotalLoadCurrent_Type())
convSysTotalLoadCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:convSysTotalLoadCurrent.setStatus(_A)
_ConvSysSystemNumber_Type=ScaledNumber
_ConvSysSystemNumber_Object=MibScalar
convSysSystemNumber=_ConvSysSystemNumber_Object((1,3,6,1,4,1,7309,5,3,2,9),_ConvSysSystemNumber_Type())
convSysSystemNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:convSysSystemNumber.setStatus(_A)
_Conformance_ObjectIdentity=ObjectIdentity
conformance=_Conformance_ObjectIdentity((1,3,6,1,4,1,7309,5,3,2,100))
_Compliances_ObjectIdentity=ObjectIdentity
compliances=_Compliances_ObjectIdentity((1,3,6,1,4,1,7309,5,3,2,100,1))
_ConverterGroups_ObjectIdentity=ObjectIdentity
converterGroups=_ConverterGroups_ObjectIdentity((1,3,6,1,4,1,7309,5,3,2,100,2))
converterGroup=ObjectGroup((1,3,6,1,4,1,7309,5,3,2,100,2,1))
converterGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:converterGroup.setStatus(_A)
compliance=ModuleCompliance((1,3,6,1,4,1,7309,5,3,2,100,1,1))
compliance.setObjects((_B,_M))
if mibBuilder.loadTexts:compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'converterSystem':converterSystem,_D:convSysTotalOutputCurrent,_E:convSysTotalOutputPower,_F:convSysTotalCapacityInstalledAmps,_G:convSysTotalCapacityInstalledPower,_H:convSysAverageConverterOutputVoltage,_I:convSysAverageConverterInputVoltage,_J:convSysSystemVoltage,_K:convSysTotalLoadCurrent,_L:convSysSystemNumber,'conformance':conformance,'compliances':compliances,'compliance':compliance,'converterGroups':converterGroups,_M:converterGroup})