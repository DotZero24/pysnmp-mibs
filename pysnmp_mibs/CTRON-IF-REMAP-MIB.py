_J='ctIfRemapDestIf'
_I='ctIfRemapSourceIf'
_H='unsupported'
_G='disable'
_F='enable'
_E='CTRON-IF-REMAP-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctIFRemap,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctIFRemap')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtIfRemapConfig_ObjectIdentity=ObjectIdentity
ctIfRemapConfig=_CtIfRemapConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,13,1))
_CtIFRemapTable_Object=MibTable
ctIFRemapTable=_CtIFRemapTable_Object((1,3,6,1,4,1,52,4,1,1,13,1,1))
if mibBuilder.loadTexts:ctIFRemapTable.setStatus(_A)
_CtIFRemapEntry_Object=MibTableRow
ctIFRemapEntry=_CtIFRemapEntry_Object((1,3,6,1,4,1,52,4,1,1,13,1,1,1))
ctIFRemapEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:ctIFRemapEntry.setStatus(_A)
_CtIfRemapSourceIf_Type=Integer32
_CtIfRemapSourceIf_Object=MibTableColumn
ctIfRemapSourceIf=_CtIfRemapSourceIf_Object((1,3,6,1,4,1,52,4,1,1,13,1,1,1,1),_CtIfRemapSourceIf_Type())
ctIfRemapSourceIf.setMaxAccess(_C)
if mibBuilder.loadTexts:ctIfRemapSourceIf.setStatus(_A)
_CtIfRemapDestIf_Type=Integer32
_CtIfRemapDestIf_Object=MibTableColumn
ctIfRemapDestIf=_CtIfRemapDestIf_Object((1,3,6,1,4,1,52,4,1,1,13,1,1,1,2),_CtIfRemapDestIf_Type())
ctIfRemapDestIf.setMaxAccess(_C)
if mibBuilder.loadTexts:ctIfRemapDestIf.setStatus(_A)
class _CtIfRemapStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CtIfRemapStatus_Type.__name__=_B
_CtIfRemapStatus_Object=MibTableColumn
ctIfRemapStatus=_CtIfRemapStatus_Object((1,3,6,1,4,1,52,4,1,1,13,1,1,1,3),_CtIfRemapStatus_Type())
ctIfRemapStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctIfRemapStatus.setStatus(_A)
_CtIfRemapTableNumberEntries_Type=Integer32
_CtIfRemapTableNumberEntries_Object=MibScalar
ctIfRemapTableNumberEntries=_CtIfRemapTableNumberEntries_Object((1,3,6,1,4,1,52,4,1,1,13,2),_CtIfRemapTableNumberEntries_Type())
ctIfRemapTableNumberEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ctIfRemapTableNumberEntries.setStatus(_A)
_CtIfRemapTableMaxNumberEntries_Type=Integer32
_CtIfRemapTableMaxNumberEntries_Object=MibScalar
ctIfRemapTableMaxNumberEntries=_CtIfRemapTableMaxNumberEntries_Object((1,3,6,1,4,1,52,4,1,1,13,3),_CtIfRemapTableMaxNumberEntries_Type())
ctIfRemapTableMaxNumberEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ctIfRemapTableMaxNumberEntries.setStatus(_A)
class _CtIfRemapPhysicalErrorsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_CtIfRemapPhysicalErrorsEnable_Type.__name__=_B
_CtIfRemapPhysicalErrorsEnable_Object=MibScalar
ctIfRemapPhysicalErrorsEnable=_CtIfRemapPhysicalErrorsEnable_Object((1,3,6,1,4,1,52,4,1,1,13,4),_CtIfRemapPhysicalErrorsEnable_Type())
ctIfRemapPhysicalErrorsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ctIfRemapPhysicalErrorsEnable.setStatus(_A)
class _CtIfRemapTableEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_CtIfRemapTableEnable_Type.__name__=_B
_CtIfRemapTableEnable_Object=MibScalar
ctIfRemapTableEnable=_CtIfRemapTableEnable_Object((1,3,6,1,4,1,52,4,1,1,13,5),_CtIfRemapTableEnable_Type())
ctIfRemapTableEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ctIfRemapTableEnable.setStatus(_A)
class _CtIfRemapTableStart_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('start',1),('stop',2),(_H,3)))
_CtIfRemapTableStart_Type.__name__=_B
_CtIfRemapTableStart_Object=MibScalar
ctIfRemapTableStart=_CtIfRemapTableStart_Object((1,3,6,1,4,1,52,4,1,1,13,6),_CtIfRemapTableStart_Type())
ctIfRemapTableStart.setMaxAccess(_D)
if mibBuilder.loadTexts:ctIfRemapTableStart.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ctIfRemapConfig':ctIfRemapConfig,'ctIFRemapTable':ctIFRemapTable,'ctIFRemapEntry':ctIFRemapEntry,_I:ctIfRemapSourceIf,_J:ctIfRemapDestIf,'ctIfRemapStatus':ctIfRemapStatus,'ctIfRemapTableNumberEntries':ctIfRemapTableNumberEntries,'ctIfRemapTableMaxNumberEntries':ctIfRemapTableMaxNumberEntries,'ctIfRemapPhysicalErrorsEnable':ctIfRemapPhysicalErrorsEnable,'ctIfRemapTableEnable':ctIfRemapTableEnable,'ctIfRemapTableStart':ctIfRemapTableStart})