_E='read-only'
_D='TruthValue'
_C='read-write'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
fsFips=ModuleIdentity((1,3,6,1,4,1,10876,101,2,63))
if mibBuilder.loadTexts:fsFips.setRevisions(('2012-09-05 00:00',))
_FsFipsConfigurations_ObjectIdentity=ObjectIdentity
fsFipsConfigurations=_FsFipsConfigurations_ObjectIdentity((1,3,6,1,4,1,10876,101,2,63,1))
class _FsFipsOperMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fips',1),('nonfips',2)))
_FsFipsOperMode_Type.__name__=_A
_FsFipsOperMode_Object=MibScalar
fsFipsOperMode=_FsFipsOperMode_Object((1,3,6,1,4,1,10876,101,2,63,1,1),_FsFipsOperMode_Type())
fsFipsOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFipsOperMode.setStatus(_B)
class _FsFipsTestAlgo_Type(Integer32):defaultValue=0
_FsFipsTestAlgo_Type.__name__=_A
_FsFipsTestAlgo_Object=MibScalar
fsFipsTestAlgo=_FsFipsTestAlgo_Object((1,3,6,1,4,1,10876,101,2,63,1,2),_FsFipsTestAlgo_Type())
fsFipsTestAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFipsTestAlgo.setStatus(_B)
class _FsfipsZeroizeCryptoKeys_Type(TruthValue):defaultValue=2
_FsfipsZeroizeCryptoKeys_Type.__name__=_D
_FsfipsZeroizeCryptoKeys_Object=MibScalar
fsfipsZeroizeCryptoKeys=_FsfipsZeroizeCryptoKeys_Object((1,3,6,1,4,1,10876,101,2,63,1,3),_FsfipsZeroizeCryptoKeys_Type())
fsfipsZeroizeCryptoKeys.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfipsZeroizeCryptoKeys.setStatus(_B)
class _FsFipsTraceLevel_Type(Integer32):defaultValue=0
_FsFipsTraceLevel_Type.__name__=_A
_FsFipsTraceLevel_Object=MibScalar
fsFipsTraceLevel=_FsFipsTraceLevel_Object((1,3,6,1,4,1,10876,101,2,63,1,4),_FsFipsTraceLevel_Type())
fsFipsTraceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFipsTraceLevel.setStatus(_B)
class _FsFipsTestExecutionResult_Type(Integer32):defaultValue=0
_FsFipsTestExecutionResult_Type.__name__=_A
_FsFipsTestExecutionResult_Object=MibScalar
fsFipsTestExecutionResult=_FsFipsTestExecutionResult_Object((1,3,6,1,4,1,10876,101,2,63,1,5),_FsFipsTestExecutionResult_Type())
fsFipsTestExecutionResult.setMaxAccess(_E)
if mibBuilder.loadTexts:fsFipsTestExecutionResult.setStatus(_B)
class _FsFipsFailedAlgorithm_Type(Integer32):defaultValue=0
_FsFipsFailedAlgorithm_Type.__name__=_A
_FsFipsFailedAlgorithm_Object=MibScalar
fsFipsFailedAlgorithm=_FsFipsFailedAlgorithm_Object((1,3,6,1,4,1,10876,101,2,63,1,6),_FsFipsFailedAlgorithm_Type())
fsFipsFailedAlgorithm.setMaxAccess(_E)
if mibBuilder.loadTexts:fsFipsFailedAlgorithm.setStatus(_B)
class _FsFipsBypassCapability_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bypassCapability',1),('noBypassCapability',2)))
_FsFipsBypassCapability_Type.__name__=_A
_FsFipsBypassCapability_Object=MibScalar
fsFipsBypassCapability=_FsFipsBypassCapability_Object((1,3,6,1,4,1,10876,101,2,63,1,7),_FsFipsBypassCapability_Type())
fsFipsBypassCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFipsBypassCapability.setStatus(_B)
mibBuilder.exportSymbols('SUPERMICRO-FIPS-MIB',**{'fsFips':fsFips,'fsFipsConfigurations':fsFipsConfigurations,'fsFipsOperMode':fsFipsOperMode,'fsFipsTestAlgo':fsFipsTestAlgo,'fsfipsZeroizeCryptoKeys':fsfipsZeroizeCryptoKeys,'fsFipsTraceLevel':fsFipsTraceLevel,'fsFipsTestExecutionResult':fsFipsTestExecutionResult,'fsFipsFailedAlgorithm':fsFipsFailedAlgorithm,'fsFipsBypassCapability':fsFipsBypassCapability})