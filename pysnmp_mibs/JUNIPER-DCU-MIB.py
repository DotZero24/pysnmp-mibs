_M='jnxDcuStatsClassName'
_L='jnxDcuStatsAddrFamily'
_K='jnxDcuStatsSrcIfIndex'
_J='jnxDCUDstClassName'
_I='jnxDCUSrcIfIndex'
_H='DisplayString'
_G='Integer32'
_F='not-accessible'
_E='SnmpAdminString'
_D='JUNIPER-DCU-MIB'
_C='deprecated'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
jnxDCUs=ModuleIdentity((1,3,6,1,4,1,2636,3,6))
if mibBuilder.loadTexts:jnxDCUs.setRevisions(('2002-12-17 00:00','2002-02-28 00:00'))
_JnxDCUsTable_Object=MibTable
jnxDCUsTable=_JnxDCUsTable_Object((1,3,6,1,4,1,2636,3,6,1))
if mibBuilder.loadTexts:jnxDCUsTable.setStatus(_C)
_JnxDCUsEntry_Object=MibTableRow
jnxDCUsEntry=_JnxDCUsEntry_Object((1,3,6,1,4,1,2636,3,6,1,1))
jnxDCUsEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:jnxDCUsEntry.setStatus(_C)
_JnxDCUSrcIfIndex_Type=InterfaceIndex
_JnxDCUSrcIfIndex_Object=MibTableColumn
jnxDCUSrcIfIndex=_JnxDCUSrcIfIndex_Object((1,3,6,1,4,1,2636,3,6,1,1,1),_JnxDCUSrcIfIndex_Type())
jnxDCUSrcIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxDCUSrcIfIndex.setStatus(_C)
class _JnxDCUDstClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_JnxDCUDstClassName_Type.__name__=_H
_JnxDCUDstClassName_Object=MibTableColumn
jnxDCUDstClassName=_JnxDCUDstClassName_Object((1,3,6,1,4,1,2636,3,6,1,1,2),_JnxDCUDstClassName_Type())
jnxDCUDstClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxDCUDstClassName.setStatus(_C)
_JnxDCUPackets_Type=Counter64
_JnxDCUPackets_Object=MibTableColumn
jnxDCUPackets=_JnxDCUPackets_Object((1,3,6,1,4,1,2636,3,6,1,1,3),_JnxDCUPackets_Type())
jnxDCUPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxDCUPackets.setStatus(_C)
_JnxDCUBytes_Type=Counter64
_JnxDCUBytes_Object=MibTableColumn
jnxDCUBytes=_JnxDCUBytes_Object((1,3,6,1,4,1,2636,3,6,1,1,4),_JnxDCUBytes_Type())
jnxDCUBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxDCUBytes.setStatus(_C)
_JnxDcuStatsTable_Object=MibTable
jnxDcuStatsTable=_JnxDcuStatsTable_Object((1,3,6,1,4,1,2636,3,6,2))
if mibBuilder.loadTexts:jnxDcuStatsTable.setStatus(_A)
_JnxDcuStatsEntry_Object=MibTableRow
jnxDcuStatsEntry=_JnxDcuStatsEntry_Object((1,3,6,1,4,1,2636,3,6,2,1))
jnxDcuStatsEntry.setIndexNames((0,_D,_K),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:jnxDcuStatsEntry.setStatus(_A)
_JnxDcuStatsSrcIfIndex_Type=InterfaceIndex
_JnxDcuStatsSrcIfIndex_Object=MibTableColumn
jnxDcuStatsSrcIfIndex=_JnxDcuStatsSrcIfIndex_Object((1,3,6,1,4,1,2636,3,6,2,1,1),_JnxDcuStatsSrcIfIndex_Type())
jnxDcuStatsSrcIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxDcuStatsSrcIfIndex.setStatus(_A)
class _JnxDcuStatsAddrFamily_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_JnxDcuStatsAddrFamily_Type.__name__=_G
_JnxDcuStatsAddrFamily_Object=MibTableColumn
jnxDcuStatsAddrFamily=_JnxDcuStatsAddrFamily_Object((1,3,6,1,4,1,2636,3,6,2,1,2),_JnxDcuStatsAddrFamily_Type())
jnxDcuStatsAddrFamily.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxDcuStatsAddrFamily.setStatus(_A)
class _JnxDcuStatsClassName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,112))
_JnxDcuStatsClassName_Type.__name__=_E
_JnxDcuStatsClassName_Object=MibTableColumn
jnxDcuStatsClassName=_JnxDcuStatsClassName_Object((1,3,6,1,4,1,2636,3,6,2,1,3),_JnxDcuStatsClassName_Type())
jnxDcuStatsClassName.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxDcuStatsClassName.setStatus(_A)
_JnxDcuStatsPackets_Type=Counter64
_JnxDcuStatsPackets_Object=MibTableColumn
jnxDcuStatsPackets=_JnxDcuStatsPackets_Object((1,3,6,1,4,1,2636,3,6,2,1,4),_JnxDcuStatsPackets_Type())
jnxDcuStatsPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxDcuStatsPackets.setStatus(_A)
_JnxDcuStatsBytes_Type=Counter64
_JnxDcuStatsBytes_Object=MibTableColumn
jnxDcuStatsBytes=_JnxDcuStatsBytes_Object((1,3,6,1,4,1,2636,3,6,2,1,5),_JnxDcuStatsBytes_Type())
jnxDcuStatsBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxDcuStatsBytes.setStatus(_A)
class _JnxDcuStatsClName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,112))
_JnxDcuStatsClName_Type.__name__=_E
_JnxDcuStatsClName_Object=MibTableColumn
jnxDcuStatsClName=_JnxDcuStatsClName_Object((1,3,6,1,4,1,2636,3,6,2,1,6),_JnxDcuStatsClName_Type())
jnxDcuStatsClName.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxDcuStatsClName.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'jnxDCUs':jnxDCUs,'jnxDCUsTable':jnxDCUsTable,'jnxDCUsEntry':jnxDCUsEntry,_I:jnxDCUSrcIfIndex,_J:jnxDCUDstClassName,'jnxDCUPackets':jnxDCUPackets,'jnxDCUBytes':jnxDCUBytes,'jnxDcuStatsTable':jnxDcuStatsTable,'jnxDcuStatsEntry':jnxDcuStatsEntry,_K:jnxDcuStatsSrcIfIndex,_L:jnxDcuStatsAddrFamily,_M:jnxDcuStatsClassName,'jnxDcuStatsPackets':jnxDcuStatsPackets,'jnxDcuStatsBytes':jnxDcuStatsBytes,'jnxDcuStatsClName':jnxDcuStatsClName})