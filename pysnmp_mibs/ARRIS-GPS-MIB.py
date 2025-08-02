_I='seconds'
_H='Integer32'
_G='Unknown Time'
_F='Unsigned32'
_E='TruthValue'
_D='read-write'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arris,=mibBuilder.importSymbols('ARRIS-MIB','arris')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_C,'PhysAddress','TextualConvention',_E)
arrisGpsMib=ModuleIdentity((1,3,6,1,4,1,4115,12))
if mibBuilder.loadTexts:arrisGpsMib.setRevisions(('2014-08-17 00:00',))
class _ArrisGpsScanOnBoot_Type(TruthValue):defaultValue=1
_ArrisGpsScanOnBoot_Type.__name__=_E
_ArrisGpsScanOnBoot_Object=MibScalar
arrisGpsScanOnBoot=_ArrisGpsScanOnBoot_Object((1,3,6,1,4,1,4115,12,1),_ArrisGpsScanOnBoot_Type())
arrisGpsScanOnBoot.setMaxAccess(_D)
if mibBuilder.loadTexts:arrisGpsScanOnBoot.setStatus(_A)
class _ArrisGpsScanPeriodically_Type(TruthValue):defaultValue=2
_ArrisGpsScanPeriodically_Type.__name__=_E
_ArrisGpsScanPeriodically_Object=MibScalar
arrisGpsScanPeriodically=_ArrisGpsScanPeriodically_Object((1,3,6,1,4,1,4115,12,2),_ArrisGpsScanPeriodically_Type())
arrisGpsScanPeriodically.setMaxAccess(_D)
if mibBuilder.loadTexts:arrisGpsScanPeriodically.setStatus(_A)
class _ArrisGpsPeriodicInterval_Type(Unsigned32):defaultValue=86400;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_ArrisGpsPeriodicInterval_Type.__name__=_F
_ArrisGpsPeriodicInterval_Object=MibScalar
arrisGpsPeriodicInterval=_ArrisGpsPeriodicInterval_Object((1,3,6,1,4,1,4115,12,3),_ArrisGpsPeriodicInterval_Type())
arrisGpsPeriodicInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:arrisGpsPeriodicInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisGpsPeriodicInterval.setUnits(_I)
class _ArrisGpsPeriodicTime_Type(DisplayString):defaultValue=OctetString(_G);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisGpsPeriodicTime_Type.__name__=_C
_ArrisGpsPeriodicTime_Object=MibScalar
arrisGpsPeriodicTime=_ArrisGpsPeriodicTime_Object((1,3,6,1,4,1,4115,12,4),_ArrisGpsPeriodicTime_Type())
arrisGpsPeriodicTime.setMaxAccess(_D)
if mibBuilder.loadTexts:arrisGpsPeriodicTime.setStatus(_A)
class _ArrisGpsPowerDownAfterSuccessfulScan_Type(TruthValue):defaultValue=1
_ArrisGpsPowerDownAfterSuccessfulScan_Type.__name__=_E
_ArrisGpsPowerDownAfterSuccessfulScan_Object=MibScalar
arrisGpsPowerDownAfterSuccessfulScan=_ArrisGpsPowerDownAfterSuccessfulScan_Object((1,3,6,1,4,1,4115,12,5),_ArrisGpsPowerDownAfterSuccessfulScan_Type())
arrisGpsPowerDownAfterSuccessfulScan.setMaxAccess(_D)
if mibBuilder.loadTexts:arrisGpsPowerDownAfterSuccessfulScan.setStatus(_A)
class _ArrisGpsScanTimeout_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_ArrisGpsScanTimeout_Type.__name__=_F
_ArrisGpsScanTimeout_Object=MibScalar
arrisGpsScanTimeout=_ArrisGpsScanTimeout_Object((1,3,6,1,4,1,4115,12,6),_ArrisGpsScanTimeout_Type())
arrisGpsScanTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:arrisGpsScanTimeout.setStatus(_A)
if mibBuilder.loadTexts:arrisGpsScanTimeout.setUnits(_I)
class _ArrisGpsScanStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('indeterminate',0),('inprogress',1),('success',2),('error',3),('errorTimeout',4)))
_ArrisGpsScanStatus_Type.__name__=_H
_ArrisGpsScanStatus_Object=MibScalar
arrisGpsScanStatus=_ArrisGpsScanStatus_Object((1,3,6,1,4,1,4115,12,7),_ArrisGpsScanStatus_Type())
arrisGpsScanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisGpsScanStatus.setStatus(_A)
class _ArrisGpsErrorDetails_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArrisGpsErrorDetails_Type.__name__=_C
_ArrisGpsErrorDetails_Object=MibScalar
arrisGpsErrorDetails=_ArrisGpsErrorDetails_Object((1,3,6,1,4,1,4115,12,8),_ArrisGpsErrorDetails_Type())
arrisGpsErrorDetails.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisGpsErrorDetails.setStatus(_A)
class _ArrisGpsLastScanTime_Type(DisplayString):defaultValue=OctetString(_G);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisGpsLastScanTime_Type.__name__=_C
_ArrisGpsLastScanTime_Object=MibScalar
arrisGpsLastScanTime=_ArrisGpsLastScanTime_Object((1,3,6,1,4,1,4115,12,9),_ArrisGpsLastScanTime_Type())
arrisGpsLastScanTime.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisGpsLastScanTime.setStatus(_A)
class _ArrisGpsLastSuccessfulScanTime_Type(DisplayString):defaultValue=OctetString(_G);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisGpsLastSuccessfulScanTime_Type.__name__=_C
_ArrisGpsLastSuccessfulScanTime_Object=MibScalar
arrisGpsLastSuccessfulScanTime=_ArrisGpsLastSuccessfulScanTime_Object((1,3,6,1,4,1,4115,12,10),_ArrisGpsLastSuccessfulScanTime_Type())
arrisGpsLastSuccessfulScanTime.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisGpsLastSuccessfulScanTime.setStatus(_A)
class _ArrisGpsLockedLatitude_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisGpsLockedLatitude_Type.__name__=_C
_ArrisGpsLockedLatitude_Object=MibScalar
arrisGpsLockedLatitude=_ArrisGpsLockedLatitude_Object((1,3,6,1,4,1,4115,12,11),_ArrisGpsLockedLatitude_Type())
arrisGpsLockedLatitude.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisGpsLockedLatitude.setStatus(_A)
class _ArrisGpsLockedLongitude_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisGpsLockedLongitude_Type.__name__=_C
_ArrisGpsLockedLongitude_Object=MibScalar
arrisGpsLockedLongitude=_ArrisGpsLockedLongitude_Object((1,3,6,1,4,1,4115,12,12),_ArrisGpsLockedLongitude_Type())
arrisGpsLockedLongitude.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisGpsLockedLongitude.setStatus(_A)
class _ArrisGpsNumberOfSatellites_Type(Unsigned32):defaultValue=0
_ArrisGpsNumberOfSatellites_Type.__name__=_F
_ArrisGpsNumberOfSatellites_Object=MibScalar
arrisGpsNumberOfSatellites=_ArrisGpsNumberOfSatellites_Object((1,3,6,1,4,1,4115,12,13),_ArrisGpsNumberOfSatellites_Type())
arrisGpsNumberOfSatellites.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisGpsNumberOfSatellites.setStatus(_A)
class _ArrisGpsReset_Type(TruthValue):defaultValue=2
_ArrisGpsReset_Type.__name__=_E
_ArrisGpsReset_Object=MibScalar
arrisGpsReset=_ArrisGpsReset_Object((1,3,6,1,4,1,4115,12,14),_ArrisGpsReset_Type())
arrisGpsReset.setMaxAccess(_D)
if mibBuilder.loadTexts:arrisGpsReset.setStatus(_A)
class _ArrisGpsSuccessfulScanSinceBootup_Type(TruthValue):defaultValue=2
_ArrisGpsSuccessfulScanSinceBootup_Type.__name__=_E
_ArrisGpsSuccessfulScanSinceBootup_Object=MibScalar
arrisGpsSuccessfulScanSinceBootup=_ArrisGpsSuccessfulScanSinceBootup_Object((1,3,6,1,4,1,4115,12,15),_ArrisGpsSuccessfulScanSinceBootup_Type())
arrisGpsSuccessfulScanSinceBootup.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisGpsSuccessfulScanSinceBootup.setStatus(_A)
mibBuilder.exportSymbols('ARRIS-GPS-MIB',**{'arrisGpsMib':arrisGpsMib,'arrisGpsScanOnBoot':arrisGpsScanOnBoot,'arrisGpsScanPeriodically':arrisGpsScanPeriodically,'arrisGpsPeriodicInterval':arrisGpsPeriodicInterval,'arrisGpsPeriodicTime':arrisGpsPeriodicTime,'arrisGpsPowerDownAfterSuccessfulScan':arrisGpsPowerDownAfterSuccessfulScan,'arrisGpsScanTimeout':arrisGpsScanTimeout,'arrisGpsScanStatus':arrisGpsScanStatus,'arrisGpsErrorDetails':arrisGpsErrorDetails,'arrisGpsLastScanTime':arrisGpsLastScanTime,'arrisGpsLastSuccessfulScanTime':arrisGpsLastSuccessfulScanTime,'arrisGpsLockedLatitude':arrisGpsLockedLatitude,'arrisGpsLockedLongitude':arrisGpsLockedLongitude,'arrisGpsNumberOfSatellites':arrisGpsNumberOfSatellites,'arrisGpsReset':arrisGpsReset,'arrisGpsSuccessfulScanSinceBootup':arrisGpsSuccessfulScanSinceBootup})