_I='read-write'
_H='nbsOpticPortNdx'
_G='NBS-OPTIC-MIB'
_F='inService'
_E='outOfService'
_D='notSupported'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsOpticMib=ModuleIdentity((1,3,6,1,4,1,629,213))
_NbsOpticPortGrp_ObjectIdentity=ObjectIdentity
nbsOpticPortGrp=_NbsOpticPortGrp_ObjectIdentity((1,3,6,1,4,1,629,213,1))
if mibBuilder.loadTexts:nbsOpticPortGrp.setStatus(_A)
_NbsOpticPortTableSize_Type=Integer32
_NbsOpticPortTableSize_Object=MibScalar
nbsOpticPortTableSize=_NbsOpticPortTableSize_Object((1,3,6,1,4,1,629,213,1,1),_NbsOpticPortTableSize_Type())
nbsOpticPortTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOpticPortTableSize.setStatus(_A)
_NbsOpticPortTable_Object=MibTable
nbsOpticPortTable=_NbsOpticPortTable_Object((1,3,6,1,4,1,629,213,1,2))
if mibBuilder.loadTexts:nbsOpticPortTable.setStatus(_A)
_NbsOpticPortEntry_Object=MibTableRow
nbsOpticPortEntry=_NbsOpticPortEntry_Object((1,3,6,1,4,1,629,213,1,2,1))
nbsOpticPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:nbsOpticPortEntry.setStatus(_A)
_NbsOpticPortNdx_Type=InterfaceIndex
_NbsOpticPortNdx_Object=MibTableColumn
nbsOpticPortNdx=_NbsOpticPortNdx_Object((1,3,6,1,4,1,629,213,1,2,1,1),_NbsOpticPortNdx_Type())
nbsOpticPortNdx.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nbsOpticPortNdx.setStatus(_A)
class _NbsOpticPortTxStatusAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_NbsOpticPortTxStatusAdmin_Type.__name__=_B
_NbsOpticPortTxStatusAdmin_Object=MibTableColumn
nbsOpticPortTxStatusAdmin=_NbsOpticPortTxStatusAdmin_Object((1,3,6,1,4,1,629,213,1,2,1,21),_NbsOpticPortTxStatusAdmin_Type())
nbsOpticPortTxStatusAdmin.setMaxAccess(_I)
if mibBuilder.loadTexts:nbsOpticPortTxStatusAdmin.setStatus(_A)
class _NbsOpticPortTxStatusOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_NbsOpticPortTxStatusOper_Type.__name__=_B
_NbsOpticPortTxStatusOper_Object=MibTableColumn
nbsOpticPortTxStatusOper=_NbsOpticPortTxStatusOper_Object((1,3,6,1,4,1,629,213,1,2,1,22),_NbsOpticPortTxStatusOper_Type())
nbsOpticPortTxStatusOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOpticPortTxStatusOper.setStatus(_A)
class _NbsOpticPortRxStatusAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_NbsOpticPortRxStatusAdmin_Type.__name__=_B
_NbsOpticPortRxStatusAdmin_Object=MibTableColumn
nbsOpticPortRxStatusAdmin=_NbsOpticPortRxStatusAdmin_Object((1,3,6,1,4,1,629,213,1,2,1,31),_NbsOpticPortRxStatusAdmin_Type())
nbsOpticPortRxStatusAdmin.setMaxAccess(_I)
if mibBuilder.loadTexts:nbsOpticPortRxStatusAdmin.setStatus(_A)
class _NbsOpticPortRxStatusOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_NbsOpticPortRxStatusOper_Type.__name__=_B
_NbsOpticPortRxStatusOper_Object=MibTableColumn
nbsOpticPortRxStatusOper=_NbsOpticPortRxStatusOper_Object((1,3,6,1,4,1,629,213,1,2,1,32),_NbsOpticPortRxStatusOper_Type())
nbsOpticPortRxStatusOper.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOpticPortRxStatusOper.setStatus(_A)
_NbsOpticPortConnector_Type=Integer32
_NbsOpticPortConnector_Object=MibTableColumn
nbsOpticPortConnector=_NbsOpticPortConnector_Object((1,3,6,1,4,1,629,213,1,2,1,41),_NbsOpticPortConnector_Type())
nbsOpticPortConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOpticPortConnector.setStatus(_A)
class _NbsOpticPortPolish_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('pc',2),('upc',3),('apc',4)))
_NbsOpticPortPolish_Type.__name__=_B
_NbsOpticPortPolish_Object=MibTableColumn
nbsOpticPortPolish=_NbsOpticPortPolish_Object((1,3,6,1,4,1,629,213,1,2,1,42),_NbsOpticPortPolish_Type())
nbsOpticPortPolish.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOpticPortPolish.setStatus(_A)
class _NbsOpticPortFiberMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),('reserved2',2),('reserved3',3),('singleMode',4),('multiMode',5)))
_NbsOpticPortFiberMode_Type.__name__=_B
_NbsOpticPortFiberMode_Object=MibTableColumn
nbsOpticPortFiberMode=_NbsOpticPortFiberMode_Object((1,3,6,1,4,1,629,213,1,2,1,51),_NbsOpticPortFiberMode_Type())
nbsOpticPortFiberMode.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOpticPortFiberMode.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'nbsOpticMib':nbsOpticMib,'nbsOpticPortGrp':nbsOpticPortGrp,'nbsOpticPortTableSize':nbsOpticPortTableSize,'nbsOpticPortTable':nbsOpticPortTable,'nbsOpticPortEntry':nbsOpticPortEntry,_H:nbsOpticPortNdx,'nbsOpticPortTxStatusAdmin':nbsOpticPortTxStatusAdmin,'nbsOpticPortTxStatusOper':nbsOpticPortTxStatusOper,'nbsOpticPortRxStatusAdmin':nbsOpticPortRxStatusAdmin,'nbsOpticPortRxStatusOper':nbsOpticPortRxStatusOper,'nbsOpticPortConnector':nbsOpticPortConnector,'nbsOpticPortPolish':nbsOpticPortPolish,'nbsOpticPortFiberMode':nbsOpticPortFiberMode})