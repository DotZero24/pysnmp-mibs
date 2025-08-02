_G='seconds'
_F='ifIndex'
_E='IF-MIB'
_D='TruthValue'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cadSystem,=mibBuilder.importSymbols('CADANT-PRODUCTS-MIB','cadSystem')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
cadBpi2Mib=ModuleIdentity((1,3,6,1,4,1,4998,1,1,5,5))
if mibBuilder.loadTexts:cadBpi2Mib.setRevisions(('2014-07-30 00:00','2006-12-18 00:00'))
_CadBpi2CmtsBaseTable_Object=MibTable
cadBpi2CmtsBaseTable=_CadBpi2CmtsBaseTable_Object((1,3,6,1,4,1,4998,1,1,5,5,1))
if mibBuilder.loadTexts:cadBpi2CmtsBaseTable.setStatus(_A)
_CadBpi2CmtsBaseEntry_Object=MibTableRow
cadBpi2CmtsBaseEntry=_CadBpi2CmtsBaseEntry_Object((1,3,6,1,4,1,4998,1,1,5,5,1,1))
cadBpi2CmtsBaseEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cadBpi2CmtsBaseEntry.setStatus(_A)
class _CadBpi2CmtsDefaultAuthLifetime_Type(Integer32):defaultValue=604800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6048000))
_CadBpi2CmtsDefaultAuthLifetime_Type.__name__=_C
_CadBpi2CmtsDefaultAuthLifetime_Object=MibTableColumn
cadBpi2CmtsDefaultAuthLifetime=_CadBpi2CmtsDefaultAuthLifetime_Object((1,3,6,1,4,1,4998,1,1,5,5,1,1,1),_CadBpi2CmtsDefaultAuthLifetime_Type())
cadBpi2CmtsDefaultAuthLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:cadBpi2CmtsDefaultAuthLifetime.setStatus(_A)
if mibBuilder.loadTexts:cadBpi2CmtsDefaultAuthLifetime.setUnits(_G)
class _CadBpi2CmtsDefaultTEKLifetime_Type(Integer32):defaultValue=43200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,604800))
_CadBpi2CmtsDefaultTEKLifetime_Type.__name__=_C
_CadBpi2CmtsDefaultTEKLifetime_Object=MibTableColumn
cadBpi2CmtsDefaultTEKLifetime=_CadBpi2CmtsDefaultTEKLifetime_Object((1,3,6,1,4,1,4998,1,1,5,5,1,1,2),_CadBpi2CmtsDefaultTEKLifetime_Type())
cadBpi2CmtsDefaultTEKLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:cadBpi2CmtsDefaultTEKLifetime.setStatus(_A)
if mibBuilder.loadTexts:cadBpi2CmtsDefaultTEKLifetime.setUnits(_G)
class _CadBpi2CmtsDefaultSelfSignedManufCertTrust_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trusted',1),('untrusted',2)))
_CadBpi2CmtsDefaultSelfSignedManufCertTrust_Type.__name__=_C
_CadBpi2CmtsDefaultSelfSignedManufCertTrust_Object=MibTableColumn
cadBpi2CmtsDefaultSelfSignedManufCertTrust=_CadBpi2CmtsDefaultSelfSignedManufCertTrust_Object((1,3,6,1,4,1,4998,1,1,5,5,1,1,3),_CadBpi2CmtsDefaultSelfSignedManufCertTrust_Type())
cadBpi2CmtsDefaultSelfSignedManufCertTrust.setMaxAccess(_B)
if mibBuilder.loadTexts:cadBpi2CmtsDefaultSelfSignedManufCertTrust.setStatus(_A)
class _CadBpi2CmtsCheckCertValidityPeriods_Type(TruthValue):defaultValue=2
_CadBpi2CmtsCheckCertValidityPeriods_Type.__name__=_D
_CadBpi2CmtsCheckCertValidityPeriods_Object=MibTableColumn
cadBpi2CmtsCheckCertValidityPeriods=_CadBpi2CmtsCheckCertValidityPeriods_Object((1,3,6,1,4,1,4998,1,1,5,5,1,1,4),_CadBpi2CmtsCheckCertValidityPeriods_Type())
cadBpi2CmtsCheckCertValidityPeriods.setMaxAccess(_B)
if mibBuilder.loadTexts:cadBpi2CmtsCheckCertValidityPeriods.setStatus(_A)
_CadBpi2CmtsConfig_ObjectIdentity=ObjectIdentity
cadBpi2CmtsConfig=_CadBpi2CmtsConfig_ObjectIdentity((1,3,6,1,4,1,4998,1,1,5,5,2))
class _CadBpi2CmtsAES128Enable_Type(TruthValue):defaultValue=2
_CadBpi2CmtsAES128Enable_Type.__name__=_D
_CadBpi2CmtsAES128Enable_Object=MibScalar
cadBpi2CmtsAES128Enable=_CadBpi2CmtsAES128Enable_Object((1,3,6,1,4,1,4998,1,1,5,5,2,1),_CadBpi2CmtsAES128Enable_Type())
cadBpi2CmtsAES128Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:cadBpi2CmtsAES128Enable.setStatus(_A)
mibBuilder.exportSymbols('CADANT-CMTS-BPI2-MIB',**{'cadBpi2Mib':cadBpi2Mib,'cadBpi2CmtsBaseTable':cadBpi2CmtsBaseTable,'cadBpi2CmtsBaseEntry':cadBpi2CmtsBaseEntry,'cadBpi2CmtsDefaultAuthLifetime':cadBpi2CmtsDefaultAuthLifetime,'cadBpi2CmtsDefaultTEKLifetime':cadBpi2CmtsDefaultTEKLifetime,'cadBpi2CmtsDefaultSelfSignedManufCertTrust':cadBpi2CmtsDefaultSelfSignedManufCertTrust,'cadBpi2CmtsCheckCertValidityPeriods':cadBpi2CmtsCheckCertValidityPeriods,'cadBpi2CmtsConfig':cadBpi2CmtsConfig,'cadBpi2CmtsAES128Enable':cadBpi2CmtsAES128Enable})