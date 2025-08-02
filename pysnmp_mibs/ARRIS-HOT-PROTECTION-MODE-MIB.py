_D='read-only'
_C='read-write'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arrisProdIdCM,=mibBuilder.importSymbols('ARRIS-MIB','arrisProdIdCM')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
arrisHorizOvertempProtModeMib=ModuleIdentity((1,3,6,1,4,1,4115,1,3,16))
if mibBuilder.loadTexts:arrisHorizOvertempProtModeMib.setRevisions(('2014-09-05 00:00','2014-09-24 00:00','2014-10-01 00:00'))
_ArrisHorizOvertempProtModeMibObjects_ObjectIdentity=ObjectIdentity
arrisHorizOvertempProtModeMibObjects=_ArrisHorizOvertempProtModeMibObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,3,16,1))
_ArrisHorizOvertempProtModeMonitoring_ObjectIdentity=ObjectIdentity
arrisHorizOvertempProtModeMonitoring=_ArrisHorizOvertempProtModeMonitoring_ObjectIdentity((1,3,6,1,4,1,4115,1,3,16,1,1))
class _ArrisHorizOvertempProtModeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('thresholdExceededHOTPTier1',2),('thresholdExceededHOTPTier2',3)))
_ArrisHorizOvertempProtModeState_Type.__name__=_A
_ArrisHorizOvertempProtModeState_Object=MibScalar
arrisHorizOvertempProtModeState=_ArrisHorizOvertempProtModeState_Object((1,3,6,1,4,1,4115,1,3,16,1,1,1),_ArrisHorizOvertempProtModeState_Type())
arrisHorizOvertempProtModeState.setMaxAccess(_D)
if mibBuilder.loadTexts:arrisHorizOvertempProtModeState.setStatus(_B)
_ArrisHorizOvertempProtModeCount_Type=Counter32
_ArrisHorizOvertempProtModeCount_Object=MibScalar
arrisHorizOvertempProtModeCount=_ArrisHorizOvertempProtModeCount_Object((1,3,6,1,4,1,4115,1,3,16,1,1,2),_ArrisHorizOvertempProtModeCount_Type())
arrisHorizOvertempProtModeCount.setMaxAccess(_D)
if mibBuilder.loadTexts:arrisHorizOvertempProtModeCount.setStatus(_B)
_ArrisHorizOvertempProtModeConfiguration_ObjectIdentity=ObjectIdentity
arrisHorizOvertempProtModeConfiguration=_ArrisHorizOvertempProtModeConfiguration_ObjectIdentity((1,3,6,1,4,1,4115,1,3,16,1,2))
class _ArrisHorizOvertempProtModeTier1MinThreshold_Type(Integer32):defaultValue=37;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,65))
_ArrisHorizOvertempProtModeTier1MinThreshold_Type.__name__=_A
_ArrisHorizOvertempProtModeTier1MinThreshold_Object=MibScalar
arrisHorizOvertempProtModeTier1MinThreshold=_ArrisHorizOvertempProtModeTier1MinThreshold_Object((1,3,6,1,4,1,4115,1,3,16,1,2,1),_ArrisHorizOvertempProtModeTier1MinThreshold_Type())
arrisHorizOvertempProtModeTier1MinThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisHorizOvertempProtModeTier1MinThreshold.setStatus(_B)
class _ArrisHorizOvertempProtModeTier1MaxThreshold_Type(Integer32):defaultValue=47;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,65))
_ArrisHorizOvertempProtModeTier1MaxThreshold_Type.__name__=_A
_ArrisHorizOvertempProtModeTier1MaxThreshold_Object=MibScalar
arrisHorizOvertempProtModeTier1MaxThreshold=_ArrisHorizOvertempProtModeTier1MaxThreshold_Object((1,3,6,1,4,1,4115,1,3,16,1,2,2),_ArrisHorizOvertempProtModeTier1MaxThreshold_Type())
arrisHorizOvertempProtModeTier1MaxThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisHorizOvertempProtModeTier1MaxThreshold.setStatus(_B)
class _ArrisHorizOvertempProtModeNormalOpRecoveryTemp_Type(Integer32):defaultValue=33;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,65))
_ArrisHorizOvertempProtModeNormalOpRecoveryTemp_Type.__name__=_A
_ArrisHorizOvertempProtModeNormalOpRecoveryTemp_Object=MibScalar
arrisHorizOvertempProtModeNormalOpRecoveryTemp=_ArrisHorizOvertempProtModeNormalOpRecoveryTemp_Object((1,3,6,1,4,1,4115,1,3,16,1,2,3),_ArrisHorizOvertempProtModeNormalOpRecoveryTemp_Type())
arrisHorizOvertempProtModeNormalOpRecoveryTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisHorizOvertempProtModeNormalOpRecoveryTemp.setStatus(_B)
mibBuilder.exportSymbols('ARRIS-HOT-PROTECTION-MODE-MIB',**{'arrisHorizOvertempProtModeMib':arrisHorizOvertempProtModeMib,'arrisHorizOvertempProtModeMibObjects':arrisHorizOvertempProtModeMibObjects,'arrisHorizOvertempProtModeMonitoring':arrisHorizOvertempProtModeMonitoring,'arrisHorizOvertempProtModeState':arrisHorizOvertempProtModeState,'arrisHorizOvertempProtModeCount':arrisHorizOvertempProtModeCount,'arrisHorizOvertempProtModeConfiguration':arrisHorizOvertempProtModeConfiguration,'arrisHorizOvertempProtModeTier1MinThreshold':arrisHorizOvertempProtModeTier1MinThreshold,'arrisHorizOvertempProtModeTier1MaxThreshold':arrisHorizOvertempProtModeTier1MaxThreshold,'arrisHorizOvertempProtModeNormalOpRecoveryTemp':arrisHorizOvertempProtModeNormalOpRecoveryTemp})