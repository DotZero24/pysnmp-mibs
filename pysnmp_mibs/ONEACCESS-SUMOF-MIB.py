_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
oacExpIMManagement,=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMManagement')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oacSumOfMIBModule=ModuleIdentity((1,3,6,1,4,1,13191,10,3,4,7))
if mibBuilder.loadTexts:oacSumOfMIBModule.setRevisions(('2011-10-27 00:00','2010-07-08 00:01'))
_OacSumOfObjects_ObjectIdentity=ObjectIdentity
oacSumOfObjects=_OacSumOfObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,7,1))
_OacSumOfIfTable_Object=MibTable
oacSumOfIfTable=_OacSumOfIfTable_Object((1,3,6,1,4,1,13191,10,3,4,7,1,1))
if mibBuilder.loadTexts:oacSumOfIfTable.setStatus(_A)
_OacSumOfIfEntry_Object=MibTableRow
oacSumOfIfEntry=_OacSumOfIfEntry_Object((1,3,6,1,4,1,13191,10,3,4,7,1,1,1))
oacSumOfIfEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:oacSumOfIfEntry.setStatus(_A)
_SumOfIfInOctets_Type=Counter32
_SumOfIfInOctets_Object=MibTableColumn
sumOfIfInOctets=_SumOfIfInOctets_Object((1,3,6,1,4,1,13191,10,3,4,7,1,1,1,1),_SumOfIfInOctets_Type())
sumOfIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfInOctets.setStatus(_A)
_SumOfIfInUcastPkts_Type=Counter32
_SumOfIfInUcastPkts_Object=MibTableColumn
sumOfIfInUcastPkts=_SumOfIfInUcastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,1,1,2),_SumOfIfInUcastPkts_Type())
sumOfIfInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfInUcastPkts.setStatus(_A)
_SumOfIfInNUcastPkts_Type=Counter32
_SumOfIfInNUcastPkts_Object=MibTableColumn
sumOfIfInNUcastPkts=_SumOfIfInNUcastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,1,1,3),_SumOfIfInNUcastPkts_Type())
sumOfIfInNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfInNUcastPkts.setStatus(_A)
_SumOfIfInDiscards_Type=Counter32
_SumOfIfInDiscards_Object=MibTableColumn
sumOfIfInDiscards=_SumOfIfInDiscards_Object((1,3,6,1,4,1,13191,10,3,4,7,1,1,1,4),_SumOfIfInDiscards_Type())
sumOfIfInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfInDiscards.setStatus(_A)
_SumOfIfInErrors_Type=Counter32
_SumOfIfInErrors_Object=MibTableColumn
sumOfIfInErrors=_SumOfIfInErrors_Object((1,3,6,1,4,1,13191,10,3,4,7,1,1,1,5),_SumOfIfInErrors_Type())
sumOfIfInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfInErrors.setStatus(_A)
_SumOfIfInUnknownProtos_Type=Counter32
_SumOfIfInUnknownProtos_Object=MibTableColumn
sumOfIfInUnknownProtos=_SumOfIfInUnknownProtos_Object((1,3,6,1,4,1,13191,10,3,4,7,1,1,1,6),_SumOfIfInUnknownProtos_Type())
sumOfIfInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfInUnknownProtos.setStatus(_A)
_SumOfIfOutOctets_Type=Counter32
_SumOfIfOutOctets_Object=MibTableColumn
sumOfIfOutOctets=_SumOfIfOutOctets_Object((1,3,6,1,4,1,13191,10,3,4,7,1,1,1,7),_SumOfIfOutOctets_Type())
sumOfIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfOutOctets.setStatus(_A)
_SumOfIfOutUcastPkts_Type=Counter32
_SumOfIfOutUcastPkts_Object=MibTableColumn
sumOfIfOutUcastPkts=_SumOfIfOutUcastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,1,1,8),_SumOfIfOutUcastPkts_Type())
sumOfIfOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfOutUcastPkts.setStatus(_A)
_SumOfIfOutNUcastPkts_Type=Counter32
_SumOfIfOutNUcastPkts_Object=MibTableColumn
sumOfIfOutNUcastPkts=_SumOfIfOutNUcastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,1,1,9),_SumOfIfOutNUcastPkts_Type())
sumOfIfOutNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfOutNUcastPkts.setStatus(_A)
_SumOfIfOutDiscards_Type=Counter32
_SumOfIfOutDiscards_Object=MibTableColumn
sumOfIfOutDiscards=_SumOfIfOutDiscards_Object((1,3,6,1,4,1,13191,10,3,4,7,1,1,1,10),_SumOfIfOutDiscards_Type())
sumOfIfOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfOutDiscards.setStatus(_A)
_SumOfIfOutErrors_Type=Counter32
_SumOfIfOutErrors_Object=MibTableColumn
sumOfIfOutErrors=_SumOfIfOutErrors_Object((1,3,6,1,4,1,13191,10,3,4,7,1,1,1,11),_SumOfIfOutErrors_Type())
sumOfIfOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfOutErrors.setStatus(_A)
_OacSumOfIfXTable_Object=MibTable
oacSumOfIfXTable=_OacSumOfIfXTable_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2))
if mibBuilder.loadTexts:oacSumOfIfXTable.setStatus(_A)
_OacSumOfIfXEntry_Object=MibTableRow
oacSumOfIfXEntry=_OacSumOfIfXEntry_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2,1))
oacSumOfIfXEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:oacSumOfIfXEntry.setStatus(_A)
_SumOfIfInMulticastPkts_Type=Counter32
_SumOfIfInMulticastPkts_Object=MibTableColumn
sumOfIfInMulticastPkts=_SumOfIfInMulticastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2,1,1),_SumOfIfInMulticastPkts_Type())
sumOfIfInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfInMulticastPkts.setStatus(_A)
_SumOfIfInBroadcastPkts_Type=Counter32
_SumOfIfInBroadcastPkts_Object=MibTableColumn
sumOfIfInBroadcastPkts=_SumOfIfInBroadcastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2,1,2),_SumOfIfInBroadcastPkts_Type())
sumOfIfInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfInBroadcastPkts.setStatus(_A)
_SumOfIfOutMulticastPkts_Type=Counter32
_SumOfIfOutMulticastPkts_Object=MibTableColumn
sumOfIfOutMulticastPkts=_SumOfIfOutMulticastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2,1,3),_SumOfIfOutMulticastPkts_Type())
sumOfIfOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfOutMulticastPkts.setStatus(_A)
_SumOfIfOutBroadcastPkts_Type=Counter32
_SumOfIfOutBroadcastPkts_Object=MibTableColumn
sumOfIfOutBroadcastPkts=_SumOfIfOutBroadcastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2,1,4),_SumOfIfOutBroadcastPkts_Type())
sumOfIfOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfOutBroadcastPkts.setStatus(_A)
_SumOfIfHCInOctets_Type=Counter64
_SumOfIfHCInOctets_Object=MibTableColumn
sumOfIfHCInOctets=_SumOfIfHCInOctets_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2,1,5),_SumOfIfHCInOctets_Type())
sumOfIfHCInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfHCInOctets.setStatus(_A)
_SumOfIfHCInUcastPkts_Type=Counter64
_SumOfIfHCInUcastPkts_Object=MibTableColumn
sumOfIfHCInUcastPkts=_SumOfIfHCInUcastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2,1,6),_SumOfIfHCInUcastPkts_Type())
sumOfIfHCInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfHCInUcastPkts.setStatus(_A)
_SumOfIfHCInMulticastPkts_Type=Counter64
_SumOfIfHCInMulticastPkts_Object=MibTableColumn
sumOfIfHCInMulticastPkts=_SumOfIfHCInMulticastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2,1,7),_SumOfIfHCInMulticastPkts_Type())
sumOfIfHCInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfHCInMulticastPkts.setStatus(_A)
_SumOfIfHCInBroadcastPkts_Type=Counter64
_SumOfIfHCInBroadcastPkts_Object=MibTableColumn
sumOfIfHCInBroadcastPkts=_SumOfIfHCInBroadcastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2,1,8),_SumOfIfHCInBroadcastPkts_Type())
sumOfIfHCInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfHCInBroadcastPkts.setStatus(_A)
_SumOfIfHCOutOctets_Type=Counter64
_SumOfIfHCOutOctets_Object=MibTableColumn
sumOfIfHCOutOctets=_SumOfIfHCOutOctets_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2,1,9),_SumOfIfHCOutOctets_Type())
sumOfIfHCOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfHCOutOctets.setStatus(_A)
_SumOfIfHCOutUcastPkts_Type=Counter64
_SumOfIfHCOutUcastPkts_Object=MibTableColumn
sumOfIfHCOutUcastPkts=_SumOfIfHCOutUcastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2,1,10),_SumOfIfHCOutUcastPkts_Type())
sumOfIfHCOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfHCOutUcastPkts.setStatus(_A)
_SumOfIfHCOutMulticastPkts_Type=Counter64
_SumOfIfHCOutMulticastPkts_Object=MibTableColumn
sumOfIfHCOutMulticastPkts=_SumOfIfHCOutMulticastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2,1,11),_SumOfIfHCOutMulticastPkts_Type())
sumOfIfHCOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfHCOutMulticastPkts.setStatus(_A)
_SumOfIfHCOutBroadcastPkts_Type=Counter64
_SumOfIfHCOutBroadcastPkts_Object=MibTableColumn
sumOfIfHCOutBroadcastPkts=_SumOfIfHCOutBroadcastPkts_Object((1,3,6,1,4,1,13191,10,3,4,7,1,2,1,12),_SumOfIfHCOutBroadcastPkts_Type())
sumOfIfHCOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sumOfIfHCOutBroadcastPkts.setStatus(_A)
mibBuilder.exportSymbols('ONEACCESS-SUMOF-MIB',**{'oacSumOfMIBModule':oacSumOfMIBModule,'oacSumOfObjects':oacSumOfObjects,'oacSumOfIfTable':oacSumOfIfTable,'oacSumOfIfEntry':oacSumOfIfEntry,'sumOfIfInOctets':sumOfIfInOctets,'sumOfIfInUcastPkts':sumOfIfInUcastPkts,'sumOfIfInNUcastPkts':sumOfIfInNUcastPkts,'sumOfIfInDiscards':sumOfIfInDiscards,'sumOfIfInErrors':sumOfIfInErrors,'sumOfIfInUnknownProtos':sumOfIfInUnknownProtos,'sumOfIfOutOctets':sumOfIfOutOctets,'sumOfIfOutUcastPkts':sumOfIfOutUcastPkts,'sumOfIfOutNUcastPkts':sumOfIfOutNUcastPkts,'sumOfIfOutDiscards':sumOfIfOutDiscards,'sumOfIfOutErrors':sumOfIfOutErrors,'oacSumOfIfXTable':oacSumOfIfXTable,'oacSumOfIfXEntry':oacSumOfIfXEntry,'sumOfIfInMulticastPkts':sumOfIfInMulticastPkts,'sumOfIfInBroadcastPkts':sumOfIfInBroadcastPkts,'sumOfIfOutMulticastPkts':sumOfIfOutMulticastPkts,'sumOfIfOutBroadcastPkts':sumOfIfOutBroadcastPkts,'sumOfIfHCInOctets':sumOfIfHCInOctets,'sumOfIfHCInUcastPkts':sumOfIfHCInUcastPkts,'sumOfIfHCInMulticastPkts':sumOfIfHCInMulticastPkts,'sumOfIfHCInBroadcastPkts':sumOfIfHCInBroadcastPkts,'sumOfIfHCOutOctets':sumOfIfHCOutOctets,'sumOfIfHCOutUcastPkts':sumOfIfHCOutUcastPkts,'sumOfIfHCOutMulticastPkts':sumOfIfHCOutMulticastPkts,'sumOfIfHCOutBroadcastPkts':sumOfIfHCOutBroadcastPkts})