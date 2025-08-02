_S='alaIpmrmDebugMIBGroup'
_R='current'
_Q='alaIpmrmDebugAll'
_P='alaIpmrmDebugMisc'
_O='alaIpmrmDebugTm'
_N='alaIpmrmDebugInit'
_M='alaIpmrmDebugMip'
_L='alaIpmrmDebugIpms'
_K='alaIpmrmDebugProtos'
_J='alaIpmrmDebugAging'
_I='alaIpmrmDebugFib'
_H='alaIpmrmDebugError'
_G='alaIpmrmDebugLevel'
_F='disable'
_E='enable'
_D='deprecated'
_C='read-write'
_B='Integer32'
_A='ALCATEL-IND1-IPMRM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Ipmrm,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','routingIND1Ipmrm')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1IPMRMMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,10,1))
if mibBuilder.loadTexts:alcatelIND1IPMRMMIB.setRevisions(('2007-04-03 00:00',))
_AlcatelIND1IPMRMMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1IPMRMMIBObjects=_AlcatelIND1IPMRMMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,1))
_AlaIpmrmDebugConfig_ObjectIdentity=ObjectIdentity
alaIpmrmDebugConfig=_AlaIpmrmDebugConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,1,1))
class _AlaIpmrmDebugLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaIpmrmDebugLevel_Type.__name__=_B
_AlaIpmrmDebugLevel_Object=MibScalar
alaIpmrmDebugLevel=_AlaIpmrmDebugLevel_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,1,1,1),_AlaIpmrmDebugLevel_Type())
alaIpmrmDebugLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpmrmDebugLevel.setStatus(_D)
class _AlaIpmrmDebugError_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaIpmrmDebugError_Type.__name__=_B
_AlaIpmrmDebugError_Object=MibScalar
alaIpmrmDebugError=_AlaIpmrmDebugError_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,1,1,2),_AlaIpmrmDebugError_Type())
alaIpmrmDebugError.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpmrmDebugError.setStatus(_D)
class _AlaIpmrmDebugFib_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaIpmrmDebugFib_Type.__name__=_B
_AlaIpmrmDebugFib_Object=MibScalar
alaIpmrmDebugFib=_AlaIpmrmDebugFib_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,1,1,3),_AlaIpmrmDebugFib_Type())
alaIpmrmDebugFib.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpmrmDebugFib.setStatus(_D)
class _AlaIpmrmDebugAging_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaIpmrmDebugAging_Type.__name__=_B
_AlaIpmrmDebugAging_Object=MibScalar
alaIpmrmDebugAging=_AlaIpmrmDebugAging_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,1,1,4),_AlaIpmrmDebugAging_Type())
alaIpmrmDebugAging.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpmrmDebugAging.setStatus(_D)
class _AlaIpmrmDebugProtos_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaIpmrmDebugProtos_Type.__name__=_B
_AlaIpmrmDebugProtos_Object=MibScalar
alaIpmrmDebugProtos=_AlaIpmrmDebugProtos_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,1,1,5),_AlaIpmrmDebugProtos_Type())
alaIpmrmDebugProtos.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpmrmDebugProtos.setStatus(_D)
class _AlaIpmrmDebugIpms_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaIpmrmDebugIpms_Type.__name__=_B
_AlaIpmrmDebugIpms_Object=MibScalar
alaIpmrmDebugIpms=_AlaIpmrmDebugIpms_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,1,1,6),_AlaIpmrmDebugIpms_Type())
alaIpmrmDebugIpms.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpmrmDebugIpms.setStatus(_D)
class _AlaIpmrmDebugMip_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaIpmrmDebugMip_Type.__name__=_B
_AlaIpmrmDebugMip_Object=MibScalar
alaIpmrmDebugMip=_AlaIpmrmDebugMip_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,1,1,7),_AlaIpmrmDebugMip_Type())
alaIpmrmDebugMip.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpmrmDebugMip.setStatus(_D)
class _AlaIpmrmDebugInit_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaIpmrmDebugInit_Type.__name__=_B
_AlaIpmrmDebugInit_Object=MibScalar
alaIpmrmDebugInit=_AlaIpmrmDebugInit_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,1,1,8),_AlaIpmrmDebugInit_Type())
alaIpmrmDebugInit.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpmrmDebugInit.setStatus(_D)
class _AlaIpmrmDebugTm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaIpmrmDebugTm_Type.__name__=_B
_AlaIpmrmDebugTm_Object=MibScalar
alaIpmrmDebugTm=_AlaIpmrmDebugTm_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,1,1,9),_AlaIpmrmDebugTm_Type())
alaIpmrmDebugTm.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpmrmDebugTm.setStatus(_D)
class _AlaIpmrmDebugMisc_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaIpmrmDebugMisc_Type.__name__=_B
_AlaIpmrmDebugMisc_Object=MibScalar
alaIpmrmDebugMisc=_AlaIpmrmDebugMisc_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,1,1,10),_AlaIpmrmDebugMisc_Type())
alaIpmrmDebugMisc.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpmrmDebugMisc.setStatus(_D)
class _AlaIpmrmDebugAll_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaIpmrmDebugAll_Type.__name__=_B
_AlaIpmrmDebugAll_Object=MibScalar
alaIpmrmDebugAll=_AlaIpmrmDebugAll_Object((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,1,1,11),_AlaIpmrmDebugAll_Type())
alaIpmrmDebugAll.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIpmrmDebugAll.setStatus(_D)
_AlcatelIND1IPMRMMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1IPMRMMIBConformance=_AlcatelIND1IPMRMMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,2))
_AlcatelIND1IPMRMMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1IPMRMMIBCompliances=_AlcatelIND1IPMRMMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,2,1))
_AlcatelIND1IPMRMMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1IPMRMMIBGroups=_AlcatelIND1IPMRMMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,2,2))
alaIpmrmDebugMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,2,2,2))
alaIpmrmDebugMIBGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:alaIpmrmDebugMIBGroup.setStatus(_R)
alaIpmrmCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,10,1,2,1,1))
alaIpmrmCompliance.setObjects((_A,_S))
if mibBuilder.loadTexts:alaIpmrmCompliance.setStatus(_R)
mibBuilder.exportSymbols(_A,**{'alcatelIND1IPMRMMIB':alcatelIND1IPMRMMIB,'alcatelIND1IPMRMMIBObjects':alcatelIND1IPMRMMIBObjects,'alaIpmrmDebugConfig':alaIpmrmDebugConfig,_G:alaIpmrmDebugLevel,_H:alaIpmrmDebugError,_I:alaIpmrmDebugFib,_J:alaIpmrmDebugAging,_K:alaIpmrmDebugProtos,_L:alaIpmrmDebugIpms,_M:alaIpmrmDebugMip,_N:alaIpmrmDebugInit,_O:alaIpmrmDebugTm,_P:alaIpmrmDebugMisc,_Q:alaIpmrmDebugAll,'alcatelIND1IPMRMMIBConformance':alcatelIND1IPMRMMIBConformance,'alcatelIND1IPMRMMIBCompliances':alcatelIND1IPMRMMIBCompliances,'alaIpmrmCompliance':alaIpmrmCompliance,'alcatelIND1IPMRMMIBGroups':alcatelIND1IPMRMMIBGroups,_S:alaIpmrmDebugMIBGroup})