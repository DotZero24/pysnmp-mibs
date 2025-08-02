_Q='hpnicfAal5NotificationGroup'
_P='hpnicfAal5MIBGroup'
_O='hpnicfAal5VccStateChange'
_N='hpnicfAal5VccState'
_M='hpnicfAal5VccOutOctets'
_L='hpnicfAal5VccInOctets'
_K='hpnicfAal5VccOutPkts'
_J='hpnicfAal5VccInPkts'
_I='not-accessible'
_H='hpnicfAal5VccVci'
_G='hpnicfAal5VccVpi'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='HPN-ICF-AAL5-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfAAL5,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfAAL5')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfAAL5MIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,21,1))
if mibBuilder.loadTexts:hpnicfAAL5MIB.setRevisions(('2004-11-04 13:50',))
_HpnicfAal5MIBTraps_ObjectIdentity=ObjectIdentity
hpnicfAal5MIBTraps=_HpnicfAal5MIBTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,21,1,0))
_HpnicfAal5MIBObjects_ObjectIdentity=ObjectIdentity
hpnicfAal5MIBObjects=_HpnicfAal5MIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,21,1,1))
_HpnicfAal5VccTable_Object=MibTable
hpnicfAal5VccTable=_HpnicfAal5VccTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,21,1,1,1))
if mibBuilder.loadTexts:hpnicfAal5VccTable.setStatus(_A)
_HpnicfAal5VccEntry_Object=MibTableRow
hpnicfAal5VccEntry=_HpnicfAal5VccEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,21,1,1,1,1))
hpnicfAal5VccEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:hpnicfAal5VccEntry.setStatus(_A)
class _HpnicfAal5VccVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_HpnicfAal5VccVpi_Type.__name__=_D
_HpnicfAal5VccVpi_Object=MibTableColumn
hpnicfAal5VccVpi=_HpnicfAal5VccVpi_Object((1,3,6,1,4,1,11,2,14,11,15,2,21,1,1,1,1,1),_HpnicfAal5VccVpi_Type())
hpnicfAal5VccVpi.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfAal5VccVpi.setStatus(_A)
class _HpnicfAal5VccVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfAal5VccVci_Type.__name__=_D
_HpnicfAal5VccVci_Object=MibTableColumn
hpnicfAal5VccVci=_HpnicfAal5VccVci_Object((1,3,6,1,4,1,11,2,14,11,15,2,21,1,1,1,1,2),_HpnicfAal5VccVci_Type())
hpnicfAal5VccVci.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfAal5VccVci.setStatus(_A)
_HpnicfAal5VccInPkts_Type=Counter32
_HpnicfAal5VccInPkts_Object=MibTableColumn
hpnicfAal5VccInPkts=_HpnicfAal5VccInPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,21,1,1,1,1,3),_HpnicfAal5VccInPkts_Type())
hpnicfAal5VccInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfAal5VccInPkts.setStatus(_A)
_HpnicfAal5VccOutPkts_Type=Counter32
_HpnicfAal5VccOutPkts_Object=MibTableColumn
hpnicfAal5VccOutPkts=_HpnicfAal5VccOutPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,21,1,1,1,1,4),_HpnicfAal5VccOutPkts_Type())
hpnicfAal5VccOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfAal5VccOutPkts.setStatus(_A)
_HpnicfAal5VccInOctets_Type=Counter32
_HpnicfAal5VccInOctets_Object=MibTableColumn
hpnicfAal5VccInOctets=_HpnicfAal5VccInOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,21,1,1,1,1,5),_HpnicfAal5VccInOctets_Type())
hpnicfAal5VccInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfAal5VccInOctets.setStatus(_A)
_HpnicfAal5VccOutOctets_Type=Counter32
_HpnicfAal5VccOutOctets_Object=MibTableColumn
hpnicfAal5VccOutOctets=_HpnicfAal5VccOutOctets_Object((1,3,6,1,4,1,11,2,14,11,15,2,21,1,1,1,1,6),_HpnicfAal5VccOutOctets_Type())
hpnicfAal5VccOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfAal5VccOutOctets.setStatus(_A)
class _HpnicfAal5VccState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalid',1),('active',2),('inactive',3)))
_HpnicfAal5VccState_Type.__name__=_D
_HpnicfAal5VccState_Object=MibTableColumn
hpnicfAal5VccState=_HpnicfAal5VccState_Object((1,3,6,1,4,1,11,2,14,11,15,2,21,1,1,1,1,7),_HpnicfAal5VccState_Type())
hpnicfAal5VccState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfAal5VccState.setStatus(_A)
_HpnicfAal5MIBConformance_ObjectIdentity=ObjectIdentity
hpnicfAal5MIBConformance=_HpnicfAal5MIBConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,21,1,3))
_HpnicfAal5MIBCompliances_ObjectIdentity=ObjectIdentity
hpnicfAal5MIBCompliances=_HpnicfAal5MIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,21,1,3,1))
_HpnicfAal5MIBGroups_ObjectIdentity=ObjectIdentity
hpnicfAal5MIBGroups=_HpnicfAal5MIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,21,1,3,2))
hpnicfAal5MIBGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,21,1,3,2,1))
hpnicfAal5MIBGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:hpnicfAal5MIBGroup.setStatus(_A)
hpnicfAal5VccStateChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,21,1,0,1))
hpnicfAal5VccStateChange.setObjects((_B,_N))
if mibBuilder.loadTexts:hpnicfAal5VccStateChange.setStatus(_A)
hpnicfAal5NotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,15,2,21,1,3,2,2))
hpnicfAal5NotificationGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:hpnicfAal5NotificationGroup.setStatus(_A)
hpnicfAal5MIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,21,1,3,1,1))
hpnicfAal5MIBCompliance.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hpnicfAal5MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfAAL5MIB':hpnicfAAL5MIB,'hpnicfAal5MIBTraps':hpnicfAal5MIBTraps,_O:hpnicfAal5VccStateChange,'hpnicfAal5MIBObjects':hpnicfAal5MIBObjects,'hpnicfAal5VccTable':hpnicfAal5VccTable,'hpnicfAal5VccEntry':hpnicfAal5VccEntry,_G:hpnicfAal5VccVpi,_H:hpnicfAal5VccVci,_J:hpnicfAal5VccInPkts,_K:hpnicfAal5VccOutPkts,_L:hpnicfAal5VccInOctets,_M:hpnicfAal5VccOutOctets,_N:hpnicfAal5VccState,'hpnicfAal5MIBConformance':hpnicfAal5MIBConformance,'hpnicfAal5MIBCompliances':hpnicfAal5MIBCompliances,'hpnicfAal5MIBCompliance':hpnicfAal5MIBCompliance,'hpnicfAal5MIBGroups':hpnicfAal5MIBGroups,_P:hpnicfAal5MIBGroup,_Q:hpnicfAal5NotificationGroup})