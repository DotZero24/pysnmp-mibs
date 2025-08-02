_I='adGenSlotInfoIndex'
_H='ADTRAN-GENSLOT-MIB'
_G='read-write'
_F='hardReset'
_E='softReset'
_D='logOnly'
_C='disabled'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_H,_I)
adGenGeminax,adGenGeminaxID=mibBuilder.importSymbols('ADTRAN-SHARED-XDSL-MIB','adGenGeminax','adGenGeminaxID')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenGeminaxMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,73,2,1))
_AdGenGeminaxMax_ObjectIdentity=ObjectIdentity
adGenGeminaxMax=_AdGenGeminaxMax_ObjectIdentity((1,3,6,1,4,1,664,5,73,2,1))
_AdGenGeminaxDiagTable_Object=MibTable
adGenGeminaxDiagTable=_AdGenGeminaxDiagTable_Object((1,3,6,1,4,1,664,5,73,2,1,1))
if mibBuilder.loadTexts:adGenGeminaxDiagTable.setStatus(_A)
_AdGenGeminaxDiagEntry_Object=MibTableRow
adGenGeminaxDiagEntry=_AdGenGeminaxDiagEntry_Object((1,3,6,1,4,1,664,5,73,2,1,1,1))
adGenGeminaxDiagEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:adGenGeminaxDiagEntry.setStatus(_A)
class _AdGenGeminaxErrorClassECF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_F,4)))
_AdGenGeminaxErrorClassECF_Type.__name__=_B
_AdGenGeminaxErrorClassECF_Object=MibTableColumn
adGenGeminaxErrorClassECF=_AdGenGeminaxErrorClassECF_Object((1,3,6,1,4,1,664,5,73,2,1,1,1,1),_AdGenGeminaxErrorClassECF_Type())
adGenGeminaxErrorClassECF.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenGeminaxErrorClassECF.setStatus(_A)
class _AdGenGeminaxErrorClassA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_F,4)))
_AdGenGeminaxErrorClassA_Type.__name__=_B
_AdGenGeminaxErrorClassA_Object=MibTableColumn
adGenGeminaxErrorClassA=_AdGenGeminaxErrorClassA_Object((1,3,6,1,4,1,664,5,73,2,1,1,1,2),_AdGenGeminaxErrorClassA_Type())
adGenGeminaxErrorClassA.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenGeminaxErrorClassA.setStatus(_A)
class _AdGenGeminaxErrorClassB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_F,4)))
_AdGenGeminaxErrorClassB_Type.__name__=_B
_AdGenGeminaxErrorClassB_Object=MibTableColumn
adGenGeminaxErrorClassB=_AdGenGeminaxErrorClassB_Object((1,3,6,1,4,1,664,5,73,2,1,1,1,3),_AdGenGeminaxErrorClassB_Type())
adGenGeminaxErrorClassB.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenGeminaxErrorClassB.setStatus(_A)
class _AdGenGeminaxErrorClassC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_F,4)))
_AdGenGeminaxErrorClassC_Type.__name__=_B
_AdGenGeminaxErrorClassC_Object=MibTableColumn
adGenGeminaxErrorClassC=_AdGenGeminaxErrorClassC_Object((1,3,6,1,4,1,664,5,73,2,1,1,1,4),_AdGenGeminaxErrorClassC_Type())
adGenGeminaxErrorClassC.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenGeminaxErrorClassC.setStatus(_A)
class _AdGenGeminaxErrorClassD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_F,4)))
_AdGenGeminaxErrorClassD_Type.__name__=_B
_AdGenGeminaxErrorClassD_Object=MibTableColumn
adGenGeminaxErrorClassD=_AdGenGeminaxErrorClassD_Object((1,3,6,1,4,1,664,5,73,2,1,1,1,5),_AdGenGeminaxErrorClassD_Type())
adGenGeminaxErrorClassD.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenGeminaxErrorClassD.setStatus(_A)
class _AdGenGeminaxErrorClassE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_F,4)))
_AdGenGeminaxErrorClassE_Type.__name__=_B
_AdGenGeminaxErrorClassE_Object=MibTableColumn
adGenGeminaxErrorClassE=_AdGenGeminaxErrorClassE_Object((1,3,6,1,4,1,664,5,73,2,1,1,1,6),_AdGenGeminaxErrorClassE_Type())
adGenGeminaxErrorClassE.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenGeminaxErrorClassE.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-GEMINAX-MIB',**{'adGenGeminaxMax':adGenGeminaxMax,'adGenGeminaxDiagTable':adGenGeminaxDiagTable,'adGenGeminaxDiagEntry':adGenGeminaxDiagEntry,'adGenGeminaxErrorClassECF':adGenGeminaxErrorClassECF,'adGenGeminaxErrorClassA':adGenGeminaxErrorClassA,'adGenGeminaxErrorClassB':adGenGeminaxErrorClassB,'adGenGeminaxErrorClassC':adGenGeminaxErrorClassC,'adGenGeminaxErrorClassD':adGenGeminaxErrorClassD,'adGenGeminaxErrorClassE':adGenGeminaxErrorClassE,'adGenGeminaxMIB':adGenGeminaxMIB})