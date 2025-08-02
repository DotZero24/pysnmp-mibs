_C='mandatory'
_B='read-only'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Tranzeo_ObjectIdentity=ObjectIdentity
tranzeo=_Tranzeo_ObjectIdentity((1,3,6,1,4,1,24575))
_Signal_ObjectIdentity=ObjectIdentity
signal=_Signal_ObjectIdentity((1,3,6,1,4,1,24575,1))
class _Rssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-110,0))
_Rssi_Type.__name__=_A
_Rssi_Object=MibScalar
rssi=_Rssi_Object((1,3,6,1,4,1,24575,1,1),_Rssi_Type())
rssi.setMaxAccess(_B)
if mibBuilder.loadTexts:rssi.setStatus(_C)
class _Signallow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-110,0))
_Signallow_Type.__name__=_A
_Signallow_Object=MibScalar
signallow=_Signallow_Object((1,3,6,1,4,1,24575,1,1,1),_Signallow_Type())
signallow.setMaxAccess(_B)
if mibBuilder.loadTexts:signallow.setStatus(_C)
class _Signalaverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-110,0))
_Signalaverage_Type.__name__=_A
_Signalaverage_Object=MibScalar
signalaverage=_Signalaverage_Object((1,3,6,1,4,1,24575,1,1,2),_Signalaverage_Type())
signalaverage.setMaxAccess(_B)
if mibBuilder.loadTexts:signalaverage.setStatus(_C)
class _Signalhigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-110,0))
_Signalhigh_Type.__name__=_A
_Signalhigh_Object=MibScalar
signalhigh=_Signalhigh_Object((1,3,6,1,4,1,24575,1,1,3),_Signalhigh_Type())
signalhigh.setMaxAccess(_B)
if mibBuilder.loadTexts:signalhigh.setStatus(_C)
class _Noise_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-110,0))
_Noise_Type.__name__=_A
_Noise_Object=MibScalar
noise=_Noise_Object((1,3,6,1,4,1,24575,1,2),_Noise_Type())
noise.setMaxAccess(_B)
if mibBuilder.loadTexts:noise.setStatus(_C)
class _Noiselow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-110,0))
_Noiselow_Type.__name__=_A
_Noiselow_Object=MibScalar
noiselow=_Noiselow_Object((1,3,6,1,4,1,24575,1,2,1),_Noiselow_Type())
noiselow.setMaxAccess(_B)
if mibBuilder.loadTexts:noiselow.setStatus(_C)
class _Noiseaverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-110,0))
_Noiseaverage_Type.__name__=_A
_Noiseaverage_Object=MibScalar
noiseaverage=_Noiseaverage_Object((1,3,6,1,4,1,24575,1,2,2),_Noiseaverage_Type())
noiseaverage.setMaxAccess(_B)
if mibBuilder.loadTexts:noiseaverage.setStatus(_C)
class _Noisehigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-110,0))
_Noisehigh_Type.__name__=_A
_Noisehigh_Object=MibScalar
noisehigh=_Noisehigh_Object((1,3,6,1,4,1,24575,1,2,3),_Noisehigh_Type())
noisehigh.setMaxAccess(_B)
if mibBuilder.loadTexts:noisehigh.setStatus(_C)
mibBuilder.exportSymbols('TRANZEO-MIB',**{'tranzeo':tranzeo,'signal':signal,'rssi':rssi,'signallow':signallow,'signalaverage':signalaverage,'signalhigh':signalhigh,'noise':noise,'noiselow':noiselow,'noiseaverage':noiseaverage,'noisehigh':noisehigh})