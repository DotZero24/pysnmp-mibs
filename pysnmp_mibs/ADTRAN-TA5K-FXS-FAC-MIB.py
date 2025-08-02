_F='read-only'
_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='OctetString'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
adTa5kFxsFac,adTa5kFxsFacID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adTa5kFxsFac','adTa5kFxsFacID')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adTa5kFxsFacIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,35,1))
if mibBuilder.loadTexts:adTa5kFxsFacIdentity.setRevisions(('2011-11-09 00:00',))
_AdTa5kFxsFacLimitedThlTable_Object=MibTable
adTa5kFxsFacLimitedThlTable=_AdTa5kFxsFacLimitedThlTable_Object((1,3,6,1,4,1,664,5,67,1,35,1))
if mibBuilder.loadTexts:adTa5kFxsFacLimitedThlTable.setStatus(_A)
_AdTa5kFxsFacLimitedThlEntry_Object=MibTableRow
adTa5kFxsFacLimitedThlEntry=_AdTa5kFxsFacLimitedThlEntry_Object((1,3,6,1,4,1,664,5,67,1,35,1,1))
adTa5kFxsFacLimitedThlEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adTa5kFxsFacLimitedThlEntry.setStatus(_A)
class _AdTa5kFxsFacLimitedThlStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('begin',1))
_AdTa5kFxsFacLimitedThlStart_Type.__name__=_B
_AdTa5kFxsFacLimitedThlStart_Object=MibTableColumn
adTa5kFxsFacLimitedThlStart=_AdTa5kFxsFacLimitedThlStart_Object((1,3,6,1,4,1,664,5,67,1,35,1,1,1),_AdTa5kFxsFacLimitedThlStart_Type())
adTa5kFxsFacLimitedThlStart.setMaxAccess('read-write')
if mibBuilder.loadTexts:adTa5kFxsFacLimitedThlStart.setStatus(_A)
class _AdTa5kFxsFacLimitedThlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('na',1),('complete',2),('fault',3),('running',4)))
_AdTa5kFxsFacLimitedThlStatus_Type.__name__=_B
_AdTa5kFxsFacLimitedThlStatus_Object=MibTableColumn
adTa5kFxsFacLimitedThlStatus=_AdTa5kFxsFacLimitedThlStatus_Object((1,3,6,1,4,1,664,5,67,1,35,1,1,2),_AdTa5kFxsFacLimitedThlStatus_Type())
adTa5kFxsFacLimitedThlStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:adTa5kFxsFacLimitedThlStatus.setStatus(_A)
class _AdTa5kFxsFacLimitedThlResults_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_AdTa5kFxsFacLimitedThlResults_Type.__name__=_C
_AdTa5kFxsFacLimitedThlResults_Object=MibTableColumn
adTa5kFxsFacLimitedThlResults=_AdTa5kFxsFacLimitedThlResults_Object((1,3,6,1,4,1,664,5,67,1,35,1,1,3),_AdTa5kFxsFacLimitedThlResults_Type())
adTa5kFxsFacLimitedThlResults.setMaxAccess(_F)
if mibBuilder.loadTexts:adTa5kFxsFacLimitedThlResults.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-TA5K-FXS-FAC-MIB',**{'adTa5kFxsFacLimitedThlTable':adTa5kFxsFacLimitedThlTable,'adTa5kFxsFacLimitedThlEntry':adTa5kFxsFacLimitedThlEntry,'adTa5kFxsFacLimitedThlStart':adTa5kFxsFacLimitedThlStart,'adTa5kFxsFacLimitedThlStatus':adTa5kFxsFacLimitedThlStatus,'adTa5kFxsFacLimitedThlResults':adTa5kFxsFacLimitedThlResults,'adTa5kFxsFacIdentity':adTa5kFxsFacIdentity})