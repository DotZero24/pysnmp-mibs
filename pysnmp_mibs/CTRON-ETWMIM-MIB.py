_G='disabled'
_F='enabled'
_E='OctetString'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctPModuleETWMIM,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctPModuleETWMIM')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class _EtwDbExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exists',1),('no-exists',2)))
_EtwDbExist_Type.__name__=_B
_EtwDbExist_Object=MibScalar
etwDbExist=_EtwDbExist_Object((1,3,6,1,4,1,52,4,1,1,4,1,1),_EtwDbExist_Type())
etwDbExist.setMaxAccess(_C)
if mibBuilder.loadTexts:etwDbExist.setStatus(_A)
class _EtwDbEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_EtwDbEnabled_Type.__name__=_B
_EtwDbEnabled_Object=MibScalar
etwDbEnabled=_EtwDbEnabled_Object((1,3,6,1,4,1,52,4,1,1,4,1,2),_EtwDbEnabled_Type())
etwDbEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:etwDbEnabled.setStatus(_A)
class _EtwDbFracToggle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('update-table',1),('display-new',2),('display-old',3),('restore-old',4)))
_EtwDbFracToggle_Type.__name__=_B
_EtwDbFracToggle_Object=MibScalar
etwDbFracToggle=_EtwDbFracToggle_Object((1,3,6,1,4,1,52,4,1,1,4,1,3),_EtwDbFracToggle_Type())
etwDbFracToggle.setMaxAccess(_D)
if mibBuilder.loadTexts:etwDbFracToggle.setStatus(_A)
class _EtwFWRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EtwFWRev_Type.__name__=_E
_EtwFWRev_Object=MibScalar
etwFWRev=_EtwFWRev_Object((1,3,6,1,4,1,52,4,1,1,4,1,4),_EtwFWRev_Type())
etwFWRev.setMaxAccess(_C)
if mibBuilder.loadTexts:etwFWRev.setStatus(_A)
_EtwHWRev_Type=Integer32
_EtwHWRev_Object=MibScalar
etwHWRev=_EtwHWRev_Object((1,3,6,1,4,1,52,4,1,1,4,1,5),_EtwHWRev_Type())
etwHWRev.setMaxAccess(_C)
if mibBuilder.loadTexts:etwHWRev.setStatus(_A)
class _EtwEpimEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_EtwEpimEnabled_Type.__name__=_B
_EtwEpimEnabled_Object=MibScalar
etwEpimEnabled=_EtwEpimEnabled_Object((1,3,6,1,4,1,52,4,1,1,4,1,6),_EtwEpimEnabled_Type())
etwEpimEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:etwEpimEnabled.setStatus(_A)
_EtwEpimType_Type=ObjectIdentifier
_EtwEpimType_Object=MibScalar
etwEpimType=_EtwEpimType_Object((1,3,6,1,4,1,52,4,1,1,4,1,7),_EtwEpimType_Type())
etwEpimType.setMaxAccess(_C)
if mibBuilder.loadTexts:etwEpimType.setStatus(_A)
class _EtwEpimLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('link-established',1),('link-not-established',2),('link-unknown',3)))
_EtwEpimLink_Type.__name__=_B
_EtwEpimLink_Object=MibScalar
etwEpimLink=_EtwEpimLink_Object((1,3,6,1,4,1,52,4,1,1,4,1,8),_EtwEpimLink_Type())
etwEpimLink.setMaxAccess(_C)
if mibBuilder.loadTexts:etwEpimLink.setStatus(_A)
_EtwClearNvramOnBoot_Type=Integer32
_EtwClearNvramOnBoot_Object=MibScalar
etwClearNvramOnBoot=_EtwClearNvramOnBoot_Object((1,3,6,1,4,1,52,4,1,1,4,1,9),_EtwClearNvramOnBoot_Type())
etwClearNvramOnBoot.setMaxAccess(_D)
if mibBuilder.loadTexts:etwClearNvramOnBoot.setStatus(_A)
mibBuilder.exportSymbols('CTRON-ETWMIM-MIB',**{'etwDbExist':etwDbExist,'etwDbEnabled':etwDbEnabled,'etwDbFracToggle':etwDbFracToggle,'etwFWRev':etwFWRev,'etwHWRev':etwHWRev,'etwEpimEnabled':etwEpimEnabled,'etwEpimType':etwEpimType,'etwEpimLink':etwEpimLink,'etwClearNvramOnBoot':etwClearNvramOnBoot})