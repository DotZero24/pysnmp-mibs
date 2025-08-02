_O='ctronMultiFnbRingIndex'
_N='ctronMultiFnbTRIndex'
_M='enable'
_L='enabled'
_K='ctronFnbTRIndex'
_J='disabled'
_I='faulted'
_H='attached'
_G='detached'
_F='CTRON-FNBTR-MIB'
_E='read-only'
_D='read-write'
_C='other'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctTokenRingFnb,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctTokenRingFnb')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtronFnbTR_ObjectIdentity=ObjectIdentity
ctronFnbTR=_CtronFnbTR_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,6,1,1))
_CtronFnbTRTable_Object=MibTable
ctronFnbTRTable=_CtronFnbTRTable_Object((1,3,6,1,4,1,52,4,1,2,6,1,1,1))
if mibBuilder.loadTexts:ctronFnbTRTable.setStatus(_A)
_CtronFnbTREntry_Object=MibTableRow
ctronFnbTREntry=_CtronFnbTREntry_Object((1,3,6,1,4,1,52,4,1,2,6,1,1,1,1))
ctronFnbTREntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:ctronFnbTREntry.setStatus(_A)
_CtronFnbTRIndex_Type=Integer32
_CtronFnbTRIndex_Object=MibTableColumn
ctronFnbTRIndex=_CtronFnbTRIndex_Object((1,3,6,1,4,1,52,4,1,2,6,1,1,1,1,1),_CtronFnbTRIndex_Type())
ctronFnbTRIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctronFnbTRIndex.setStatus(_A)
class _CtronFnbConnectLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_G,2),(_H,3),(_I,4)))
_CtronFnbConnectLeft_Type.__name__=_B
_CtronFnbConnectLeft_Object=MibTableColumn
ctronFnbConnectLeft=_CtronFnbConnectLeft_Object((1,3,6,1,4,1,52,4,1,2,6,1,1,1,1,2),_CtronFnbConnectLeft_Type())
ctronFnbConnectLeft.setMaxAccess(_D)
if mibBuilder.loadTexts:ctronFnbConnectLeft.setStatus(_A)
class _CtronFnbConnectRight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_G,2),(_H,3),(_I,4)))
_CtronFnbConnectRight_Type.__name__=_B
_CtronFnbConnectRight_Object=MibTableColumn
ctronFnbConnectRight=_CtronFnbConnectRight_Object((1,3,6,1,4,1,52,4,1,2,6,1,1,1,1,3),_CtronFnbConnectRight_Type())
ctronFnbConnectRight.setMaxAccess(_D)
if mibBuilder.loadTexts:ctronFnbConnectRight.setStatus(_A)
class _CtronFnbBypass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),(_J,2),(_L,3)))
_CtronFnbBypass_Type.__name__=_B
_CtronFnbBypass_Object=MibTableColumn
ctronFnbBypass=_CtronFnbBypass_Object((1,3,6,1,4,1,52,4,1,2,6,1,1,1,1,4),_CtronFnbBypass_Type())
ctronFnbBypass.setMaxAccess(_D)
if mibBuilder.loadTexts:ctronFnbBypass.setStatus(_A)
class _CtronFnbRPBypass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),(_M,2),(_J,3)))
_CtronFnbRPBypass_Type.__name__=_B
_CtronFnbRPBypass_Object=MibTableColumn
ctronFnbRPBypass=_CtronFnbRPBypass_Object((1,3,6,1,4,1,52,4,1,2,6,1,1,1,1,5),_CtronFnbRPBypass_Type())
ctronFnbRPBypass.setMaxAccess(_D)
if mibBuilder.loadTexts:ctronFnbRPBypass.setStatus(_A)
_CtronMultiFnbTR_ObjectIdentity=ObjectIdentity
ctronMultiFnbTR=_CtronMultiFnbTR_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,6,1,2))
_CtronMultiFnbTRTable_Object=MibTable
ctronMultiFnbTRTable=_CtronMultiFnbTRTable_Object((1,3,6,1,4,1,52,4,1,2,6,1,2,1))
if mibBuilder.loadTexts:ctronMultiFnbTRTable.setStatus(_A)
_CtronMultiFnbTREntry_Object=MibTableRow
ctronMultiFnbTREntry=_CtronMultiFnbTREntry_Object((1,3,6,1,4,1,52,4,1,2,6,1,2,1,1))
ctronMultiFnbTREntry.setIndexNames((0,_F,_N),(0,_F,_O))
if mibBuilder.loadTexts:ctronMultiFnbTREntry.setStatus(_A)
_CtronMultiFnbTRIndex_Type=Integer32
_CtronMultiFnbTRIndex_Object=MibTableColumn
ctronMultiFnbTRIndex=_CtronMultiFnbTRIndex_Object((1,3,6,1,4,1,52,4,1,2,6,1,2,1,1,1),_CtronMultiFnbTRIndex_Type())
ctronMultiFnbTRIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctronMultiFnbTRIndex.setStatus(_A)
_CtronMultiFnbRingIndex_Type=Integer32
_CtronMultiFnbRingIndex_Object=MibTableColumn
ctronMultiFnbRingIndex=_CtronMultiFnbRingIndex_Object((1,3,6,1,4,1,52,4,1,2,6,1,2,1,1,2),_CtronMultiFnbRingIndex_Type())
ctronMultiFnbRingIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctronMultiFnbRingIndex.setStatus(_A)
class _CtronMultiFnbConnectLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_G,2),(_H,3),(_I,4)))
_CtronMultiFnbConnectLeft_Type.__name__=_B
_CtronMultiFnbConnectLeft_Object=MibTableColumn
ctronMultiFnbConnectLeft=_CtronMultiFnbConnectLeft_Object((1,3,6,1,4,1,52,4,1,2,6,1,2,1,1,3),_CtronMultiFnbConnectLeft_Type())
ctronMultiFnbConnectLeft.setMaxAccess(_E)
if mibBuilder.loadTexts:ctronMultiFnbConnectLeft.setStatus(_A)
class _CtronMultiFnbConnectRight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),(_G,2),(_H,3),(_I,4)))
_CtronMultiFnbConnectRight_Type.__name__=_B
_CtronMultiFnbConnectRight_Object=MibTableColumn
ctronMultiFnbConnectRight=_CtronMultiFnbConnectRight_Object((1,3,6,1,4,1,52,4,1,2,6,1,2,1,1,4),_CtronMultiFnbConnectRight_Type())
ctronMultiFnbConnectRight.setMaxAccess(_E)
if mibBuilder.loadTexts:ctronMultiFnbConnectRight.setStatus(_A)
class _CtronMultiFnbBypass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),(_J,2),(_L,3)))
_CtronMultiFnbBypass_Type.__name__=_B
_CtronMultiFnbBypass_Object=MibTableColumn
ctronMultiFnbBypass=_CtronMultiFnbBypass_Object((1,3,6,1,4,1,52,4,1,2,6,1,2,1,1,5),_CtronMultiFnbBypass_Type())
ctronMultiFnbBypass.setMaxAccess(_D)
if mibBuilder.loadTexts:ctronMultiFnbBypass.setStatus(_A)
class _CtronMultiFnbRPBypass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_C,1),(_M,2),(_J,3)))
_CtronMultiFnbRPBypass_Type.__name__=_B
_CtronMultiFnbRPBypass_Object=MibTableColumn
ctronMultiFnbRPBypass=_CtronMultiFnbRPBypass_Object((1,3,6,1,4,1,52,4,1,2,6,1,2,1,1,6),_CtronMultiFnbRPBypass_Type())
ctronMultiFnbRPBypass.setMaxAccess(_D)
if mibBuilder.loadTexts:ctronMultiFnbRPBypass.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ctronFnbTR':ctronFnbTR,'ctronFnbTRTable':ctronFnbTRTable,'ctronFnbTREntry':ctronFnbTREntry,_K:ctronFnbTRIndex,'ctronFnbConnectLeft':ctronFnbConnectLeft,'ctronFnbConnectRight':ctronFnbConnectRight,'ctronFnbBypass':ctronFnbBypass,'ctronFnbRPBypass':ctronFnbRPBypass,'ctronMultiFnbTR':ctronMultiFnbTR,'ctronMultiFnbTRTable':ctronMultiFnbTRTable,'ctronMultiFnbTREntry':ctronMultiFnbTREntry,_N:ctronMultiFnbTRIndex,_O:ctronMultiFnbRingIndex,'ctronMultiFnbConnectLeft':ctronMultiFnbConnectLeft,'ctronMultiFnbConnectRight':ctronMultiFnbConnectRight,'ctronMultiFnbBypass':ctronMultiFnbBypass,'ctronMultiFnbRPBypass':ctronMultiFnbRPBypass})