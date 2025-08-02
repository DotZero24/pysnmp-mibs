_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='read-only'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
adGenTa5kErrorOid,adGenTa5kSErrorOidID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenTa5kErrorOid','adGenTa5kSErrorOidID')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','TextualConvention')
adGenCommonErrorOidMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,9,1))
_AdTa5kErrorOidMgmt_ObjectIdentity=ObjectIdentity
adTa5kErrorOidMgmt=_AdTa5kErrorOidMgmt_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,9,1))
_AdTa5kErrorOidTable_Object=MibTable
adTa5kErrorOidTable=_AdTa5kErrorOidTable_Object((1,3,6,1,4,1,664,5,67,1,9,1,1))
if mibBuilder.loadTexts:adTa5kErrorOidTable.setStatus(_A)
_AdTa5kErrorOidTableEntry_Object=MibTableRow
adTa5kErrorOidTableEntry=_AdTa5kErrorOidTableEntry_Object((1,3,6,1,4,1,664,5,67,1,9,1,1,1))
adTa5kErrorOidTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adTa5kErrorOidTableEntry.setStatus(_A)
class _AdTa5kDuplicateIndexErrorReporting_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AdTa5kDuplicateIndexErrorReporting_Type.__name__=_B
_AdTa5kDuplicateIndexErrorReporting_Object=MibTableColumn
adTa5kDuplicateIndexErrorReporting=_AdTa5kDuplicateIndexErrorReporting_Object((1,3,6,1,4,1,664,5,67,1,9,1,1,1,1),_AdTa5kDuplicateIndexErrorReporting_Type())
adTa5kDuplicateIndexErrorReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kDuplicateIndexErrorReporting.setStatus(_A)
class _AdTa5kPseudowireErrorReporting_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AdTa5kPseudowireErrorReporting_Type.__name__=_B
_AdTa5kPseudowireErrorReporting_Object=MibTableColumn
adTa5kPseudowireErrorReporting=_AdTa5kPseudowireErrorReporting_Object((1,3,6,1,4,1,664,5,67,1,9,1,1,1,2),_AdTa5kPseudowireErrorReporting_Type())
adTa5kPseudowireErrorReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kPseudowireErrorReporting.setStatus(_A)
class _AdTa5kPhysicalDs1ErrorReporting_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AdTa5kPhysicalDs1ErrorReporting_Type.__name__=_B
_AdTa5kPhysicalDs1ErrorReporting_Object=MibTableColumn
adTa5kPhysicalDs1ErrorReporting=_AdTa5kPhysicalDs1ErrorReporting_Object((1,3,6,1,4,1,664,5,67,1,9,1,1,1,3),_AdTa5kPhysicalDs1ErrorReporting_Type())
adTa5kPhysicalDs1ErrorReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:adTa5kPhysicalDs1ErrorReporting.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-COMMON-ERROR-OID-MIB',**{'adTa5kErrorOidMgmt':adTa5kErrorOidMgmt,'adTa5kErrorOidTable':adTa5kErrorOidTable,'adTa5kErrorOidTableEntry':adTa5kErrorOidTableEntry,'adTa5kDuplicateIndexErrorReporting':adTa5kDuplicateIndexErrorReporting,'adTa5kPseudowireErrorReporting':adTa5kPseudowireErrorReporting,'adTa5kPhysicalDs1ErrorReporting':adTa5kPhysicalDs1ErrorReporting,'adGenCommonErrorOidMIB':adGenCommonErrorOidMIB})