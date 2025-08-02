_G='mandatory'
_F='read-write'
_E='NotificationType'
_D='rndErrorSeverity'
_C='rndErrorDesc'
_B='Integer32'
_A='RADWARE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rndErrorDesc,rndErrorSeverity,rsDOS=mibBuilder.importSymbols(_A,_C,_D,'rsDOS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class _RsDOSSamplingRatio_Type(Integer32):defaultValue=100
_RsDOSSamplingRatio_Type.__name__=_B
_RsDOSSamplingRatio_Object=MibScalar
rsDOSSamplingRatio=_RsDOSSamplingRatio_Object((1,3,6,1,4,1,89,35,1,117,1),_RsDOSSamplingRatio_Type())
rsDOSSamplingRatio.setMaxAccess(_F)
if mibBuilder.loadTexts:rsDOSSamplingRatio.setStatus(_G)
class _RsDOSSamplerOverloadMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forward',1),('discard',2)))
_RsDOSSamplerOverloadMode_Type.__name__=_B
_RsDOSSamplerOverloadMode_Object=MibScalar
rsDOSSamplerOverloadMode=_RsDOSSamplerOverloadMode_Object((1,3,6,1,4,1,89,35,1,117,2),_RsDOSSamplerOverloadMode_Type())
rsDOSSamplerOverloadMode.setMaxAccess(_F)
if mibBuilder.loadTexts:rsDOSSamplerOverloadMode.setStatus(_G)
rsDOSOverloadTrap=NotificationType((1,3,6,1,4,1,89,35,1,117,0,1))
rsDOSOverloadTrap.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:rsDOSOverloadTrap.setStatus('')
mibBuilder.exportSymbols('DOS-MIB',**{'rsDOSOverloadTrap':rsDOSOverloadTrap,'rsDOSSamplingRatio':rsDOSSamplingRatio,'rsDOSSamplerOverloadMode':rsDOSSamplerOverloadMode})