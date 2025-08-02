_E='read-only'
_D='Integer32'
_C='adGenSlotInfoIndex'
_B='ADTRAN-GENSLOT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_B,_C)
adGenTa5kHk,adGenTa5kHkID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenTa5kHk','adGenTa5kHkID')
adIdentity,adIdentityShared,adMgmt,adProducts=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity','adIdentityShared','adMgmt','adProducts')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
adTa5kHkModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,7,1))
_AdTa5kHkTable_Object=MibTable
adTa5kHkTable=_AdTa5kHkTable_Object((1,3,6,1,4,1,664,5,67,1,7,1))
if mibBuilder.loadTexts:adTa5kHkTable.setStatus(_A)
_AdTa5kHkEntry_Object=MibTableRow
adTa5kHkEntry=_AdTa5kHkEntry_Object((1,3,6,1,4,1,664,5,67,1,7,1,1))
adTa5kHkEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:adTa5kHkEntry.setStatus(_A)
class _AdTa5kHkPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_AdTa5kHkPresent_Type.__name__=_D
_AdTa5kHkPresent_Object=MibTableColumn
adTa5kHkPresent=_AdTa5kHkPresent_Object((1,3,6,1,4,1,664,5,67,1,7,1,1,1),_AdTa5kHkPresent_Type())
adTa5kHkPresent.setMaxAccess(_E)
if mibBuilder.loadTexts:adTa5kHkPresent.setStatus(_A)
_AdTa5kHkTemp_Type=Integer32
_AdTa5kHkTemp_Object=MibTableColumn
adTa5kHkTemp=_AdTa5kHkTemp_Object((1,3,6,1,4,1,664,5,67,1,7,1,1,2),_AdTa5kHkTemp_Type())
adTa5kHkTemp.setMaxAccess(_E)
if mibBuilder.loadTexts:adTa5kHkTemp.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-TA5K-HK-MIB',**{'adTa5kHkTable':adTa5kHkTable,'adTa5kHkEntry':adTa5kHkEntry,'adTa5kHkPresent':adTa5kHkPresent,'adTa5kHkTemp':adTa5kHkTemp,'adTa5kHkModuleIdentity':adTa5kHkModuleIdentity})