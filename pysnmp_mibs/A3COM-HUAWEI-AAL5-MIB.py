_Q='h3cAal5NotificationGroup'
_P='h3cAal5MIBGroup'
_O='h3cAal5VccStateChange'
_N='h3cAal5VccState'
_M='h3cAal5VccOutOctets'
_L='h3cAal5VccInOctets'
_K='h3cAal5VccOutPkts'
_J='h3cAal5VccInPkts'
_I='not-accessible'
_H='h3cAal5VccVci'
_G='h3cAal5VccVpi'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='A3COM-HUAWEI-AAL5-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cAAL5,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cAAL5')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cAAL5MIB=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,21,1))
if mibBuilder.loadTexts:h3cAAL5MIB.setRevisions(('2004-11-04 13:50',))
_H3cAal5MIBTraps_ObjectIdentity=ObjectIdentity
h3cAal5MIBTraps=_H3cAal5MIBTraps_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,21,1,0))
_H3cAal5MIBObjects_ObjectIdentity=ObjectIdentity
h3cAal5MIBObjects=_H3cAal5MIBObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,21,1,1))
_H3cAal5VccTable_Object=MibTable
h3cAal5VccTable=_H3cAal5VccTable_Object((1,3,6,1,4,1,43,45,1,10,2,21,1,1,1))
if mibBuilder.loadTexts:h3cAal5VccTable.setStatus(_A)
_H3cAal5VccEntry_Object=MibTableRow
h3cAal5VccEntry=_H3cAal5VccEntry_Object((1,3,6,1,4,1,43,45,1,10,2,21,1,1,1,1))
h3cAal5VccEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:h3cAal5VccEntry.setStatus(_A)
class _H3cAal5VccVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_H3cAal5VccVpi_Type.__name__=_D
_H3cAal5VccVpi_Object=MibTableColumn
h3cAal5VccVpi=_H3cAal5VccVpi_Object((1,3,6,1,4,1,43,45,1,10,2,21,1,1,1,1,1),_H3cAal5VccVpi_Type())
h3cAal5VccVpi.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cAal5VccVpi.setStatus(_A)
class _H3cAal5VccVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cAal5VccVci_Type.__name__=_D
_H3cAal5VccVci_Object=MibTableColumn
h3cAal5VccVci=_H3cAal5VccVci_Object((1,3,6,1,4,1,43,45,1,10,2,21,1,1,1,1,2),_H3cAal5VccVci_Type())
h3cAal5VccVci.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cAal5VccVci.setStatus(_A)
_H3cAal5VccInPkts_Type=Counter32
_H3cAal5VccInPkts_Object=MibTableColumn
h3cAal5VccInPkts=_H3cAal5VccInPkts_Object((1,3,6,1,4,1,43,45,1,10,2,21,1,1,1,1,3),_H3cAal5VccInPkts_Type())
h3cAal5VccInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cAal5VccInPkts.setStatus(_A)
_H3cAal5VccOutPkts_Type=Counter32
_H3cAal5VccOutPkts_Object=MibTableColumn
h3cAal5VccOutPkts=_H3cAal5VccOutPkts_Object((1,3,6,1,4,1,43,45,1,10,2,21,1,1,1,1,4),_H3cAal5VccOutPkts_Type())
h3cAal5VccOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cAal5VccOutPkts.setStatus(_A)
_H3cAal5VccInOctets_Type=Counter32
_H3cAal5VccInOctets_Object=MibTableColumn
h3cAal5VccInOctets=_H3cAal5VccInOctets_Object((1,3,6,1,4,1,43,45,1,10,2,21,1,1,1,1,5),_H3cAal5VccInOctets_Type())
h3cAal5VccInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cAal5VccInOctets.setStatus(_A)
_H3cAal5VccOutOctets_Type=Counter32
_H3cAal5VccOutOctets_Object=MibTableColumn
h3cAal5VccOutOctets=_H3cAal5VccOutOctets_Object((1,3,6,1,4,1,43,45,1,10,2,21,1,1,1,1,6),_H3cAal5VccOutOctets_Type())
h3cAal5VccOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cAal5VccOutOctets.setStatus(_A)
class _H3cAal5VccState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalid',1),('active',2),('inactive',3)))
_H3cAal5VccState_Type.__name__=_D
_H3cAal5VccState_Object=MibTableColumn
h3cAal5VccState=_H3cAal5VccState_Object((1,3,6,1,4,1,43,45,1,10,2,21,1,1,1,1,7),_H3cAal5VccState_Type())
h3cAal5VccState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cAal5VccState.setStatus(_A)
_H3cAal5MIBConformance_ObjectIdentity=ObjectIdentity
h3cAal5MIBConformance=_H3cAal5MIBConformance_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,21,1,3))
_H3cAal5MIBCompliances_ObjectIdentity=ObjectIdentity
h3cAal5MIBCompliances=_H3cAal5MIBCompliances_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,21,1,3,1))
_H3cAal5MIBGroups_ObjectIdentity=ObjectIdentity
h3cAal5MIBGroups=_H3cAal5MIBGroups_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,21,1,3,2))
h3cAal5MIBGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,21,1,3,2,1))
h3cAal5MIBGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:h3cAal5MIBGroup.setStatus(_A)
h3cAal5VccStateChange=NotificationType((1,3,6,1,4,1,43,45,1,10,2,21,1,0,1))
h3cAal5VccStateChange.setObjects((_B,_N))
if mibBuilder.loadTexts:h3cAal5VccStateChange.setStatus(_A)
h3cAal5NotificationGroup=NotificationGroup((1,3,6,1,4,1,43,45,1,10,2,21,1,3,2,2))
h3cAal5NotificationGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:h3cAal5NotificationGroup.setStatus(_A)
h3cAal5MIBCompliance=ModuleCompliance((1,3,6,1,4,1,43,45,1,10,2,21,1,3,1,1))
h3cAal5MIBCompliance.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:h3cAal5MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cAAL5MIB':h3cAAL5MIB,'h3cAal5MIBTraps':h3cAal5MIBTraps,_O:h3cAal5VccStateChange,'h3cAal5MIBObjects':h3cAal5MIBObjects,'h3cAal5VccTable':h3cAal5VccTable,'h3cAal5VccEntry':h3cAal5VccEntry,_G:h3cAal5VccVpi,_H:h3cAal5VccVci,_J:h3cAal5VccInPkts,_K:h3cAal5VccOutPkts,_L:h3cAal5VccInOctets,_M:h3cAal5VccOutOctets,_N:h3cAal5VccState,'h3cAal5MIBConformance':h3cAal5MIBConformance,'h3cAal5MIBCompliances':h3cAal5MIBCompliances,'h3cAal5MIBCompliance':h3cAal5MIBCompliance,'h3cAal5MIBGroups':h3cAal5MIBGroups,_P:h3cAal5MIBGroup,_Q:h3cAal5NotificationGroup})