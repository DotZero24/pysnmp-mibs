_G='auxiliaryDVIndex'
_F='not-accessible'
_E='installedDVIndex'
_D='TPT-MULTIDV-MIB'
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
policyDVObjs,=mibBuilder.importSymbols('TPT-POLICY-MIB','policyDVObjs')
tpt_multidv_objs=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,1,10,2))
if mibBuilder.loadTexts:tpt_multidv_objs.setRevisions(('2016-05-25 18:54',))
class DVIsActive(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),('active',1)))
_InstalledDVTable_Object=MibTable
installedDVTable=_InstalledDVTable_Object((1,3,6,1,4,1,10734,3,3,2,1,10,2,1))
if mibBuilder.loadTexts:installedDVTable.setStatus(_A)
_InstalledDVEntry_Object=MibTableRow
installedDVEntry=_InstalledDVEntry_Object((1,3,6,1,4,1,10734,3,3,2,1,10,2,1,1))
installedDVEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:installedDVEntry.setStatus(_A)
_InstalledDVIndex_Type=Unsigned32
_InstalledDVIndex_Object=MibTableColumn
installedDVIndex=_InstalledDVIndex_Object((1,3,6,1,4,1,10734,3,3,2,1,10,2,1,1,1),_InstalledDVIndex_Type())
installedDVIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:installedDVIndex.setStatus(_A)
class _InstalledDVVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_InstalledDVVersion_Type.__name__=_C
_InstalledDVVersion_Object=MibTableColumn
installedDVVersion=_InstalledDVVersion_Object((1,3,6,1,4,1,10734,3,3,2,1,10,2,1,1,2),_InstalledDVVersion_Type())
installedDVVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:installedDVVersion.setStatus(_A)
_InstalledDVIsActive_Type=DVIsActive
_InstalledDVIsActive_Object=MibTableColumn
installedDVIsActive=_InstalledDVIsActive_Object((1,3,6,1,4,1,10734,3,3,2,1,10,2,1,1,3),_InstalledDVIsActive_Type())
installedDVIsActive.setMaxAccess(_B)
if mibBuilder.loadTexts:installedDVIsActive.setStatus(_A)
_AuxiliaryDVTable_Object=MibTable
auxiliaryDVTable=_AuxiliaryDVTable_Object((1,3,6,1,4,1,10734,3,3,2,1,10,2,2))
if mibBuilder.loadTexts:auxiliaryDVTable.setStatus(_A)
_AuxiliaryDVEntry_Object=MibTableRow
auxiliaryDVEntry=_AuxiliaryDVEntry_Object((1,3,6,1,4,1,10734,3,3,2,1,10,2,2,1))
auxiliaryDVEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:auxiliaryDVEntry.setStatus(_A)
_AuxiliaryDVIndex_Type=Unsigned32
_AuxiliaryDVIndex_Object=MibTableColumn
auxiliaryDVIndex=_AuxiliaryDVIndex_Object((1,3,6,1,4,1,10734,3,3,2,1,10,2,2,1,1),_AuxiliaryDVIndex_Type())
auxiliaryDVIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:auxiliaryDVIndex.setStatus(_A)
class _AuxiliaryDVType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_AuxiliaryDVType_Type.__name__=_C
_AuxiliaryDVType_Object=MibTableColumn
auxiliaryDVType=_AuxiliaryDVType_Object((1,3,6,1,4,1,10734,3,3,2,1,10,2,2,1,2),_AuxiliaryDVType_Type())
auxiliaryDVType.setMaxAccess(_B)
if mibBuilder.loadTexts:auxiliaryDVType.setStatus(_A)
class _AuxiliaryDVName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AuxiliaryDVName_Type.__name__=_C
_AuxiliaryDVName_Object=MibTableColumn
auxiliaryDVName=_AuxiliaryDVName_Object((1,3,6,1,4,1,10734,3,3,2,1,10,2,2,1,3),_AuxiliaryDVName_Type())
auxiliaryDVName.setMaxAccess(_B)
if mibBuilder.loadTexts:auxiliaryDVName.setStatus(_A)
_AuxiliaryDVVersion_Type=Integer32
_AuxiliaryDVVersion_Object=MibTableColumn
auxiliaryDVVersion=_AuxiliaryDVVersion_Object((1,3,6,1,4,1,10734,3,3,2,1,10,2,2,1,4),_AuxiliaryDVVersion_Type())
auxiliaryDVVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:auxiliaryDVVersion.setStatus(_A)
class _AuxiliaryDVPackage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AuxiliaryDVPackage_Type.__name__=_C
_AuxiliaryDVPackage_Object=MibTableColumn
auxiliaryDVPackage=_AuxiliaryDVPackage_Object((1,3,6,1,4,1,10734,3,3,2,1,10,2,2,1,5),_AuxiliaryDVPackage_Type())
auxiliaryDVPackage.setMaxAccess(_B)
if mibBuilder.loadTexts:auxiliaryDVPackage.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'DVIsActive':DVIsActive,'tpt-multidv-objs':tpt_multidv_objs,'installedDVTable':installedDVTable,'installedDVEntry':installedDVEntry,_E:installedDVIndex,'installedDVVersion':installedDVVersion,'installedDVIsActive':installedDVIsActive,'auxiliaryDVTable':auxiliaryDVTable,'auxiliaryDVEntry':auxiliaryDVEntry,_G:auxiliaryDVIndex,'auxiliaryDVType':auxiliaryDVType,'auxiliaryDVName':auxiliaryDVName,'auxiliaryDVVersion':auxiliaryDVVersion,'auxiliaryDVPackage':auxiliaryDVPackage})