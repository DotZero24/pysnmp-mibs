_H='atmDxiDFAConfDfaIndex'
_G='atmDxiDFAConfIfIndex'
_F='read-write'
_E='atmDxiConfIfIndex'
_D='read-only'
_C='Integer32'
_B='ATM-DXI-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class Dfa(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
_AtmForum_ObjectIdentity=ObjectIdentity
atmForum=_AtmForum_ObjectIdentity((1,3,6,1,4,1,353))
_AtmUniDxi_ObjectIdentity=ObjectIdentity
atmUniDxi=_AtmUniDxi_ObjectIdentity((1,3,6,1,4,1,353,3))
_AtmDxi_ObjectIdentity=ObjectIdentity
atmDxi=_AtmDxi_ObjectIdentity((1,3,6,1,4,1,353,3,2))
_AtmDxiConfTable_Object=MibTable
atmDxiConfTable=_AtmDxiConfTable_Object((1,3,6,1,4,1,353,3,2,2))
if mibBuilder.loadTexts:atmDxiConfTable.setStatus(_A)
_AtmDxiConfEntry_Object=MibTableRow
atmDxiConfEntry=_AtmDxiConfEntry_Object((1,3,6,1,4,1,353,3,2,2,1))
atmDxiConfEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:atmDxiConfEntry.setStatus(_A)
_AtmDxiConfIfIndex_Type=Integer32
_AtmDxiConfIfIndex_Object=MibTableColumn
atmDxiConfIfIndex=_AtmDxiConfIfIndex_Object((1,3,6,1,4,1,353,3,2,2,1,2),_AtmDxiConfIfIndex_Type())
atmDxiConfIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atmDxiConfIfIndex.setStatus(_A)
class _AtmDxiConfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mode1a',1),('mode1b',2),('mode2',3)))
_AtmDxiConfMode_Type.__name__=_C
_AtmDxiConfMode_Object=MibTableColumn
atmDxiConfMode=_AtmDxiConfMode_Object((1,3,6,1,4,1,353,3,2,2,1,3),_AtmDxiConfMode_Type())
atmDxiConfMode.setMaxAccess(_F)
if mibBuilder.loadTexts:atmDxiConfMode.setStatus(_A)
_AtmDxiDFAConfTable_Object=MibTable
atmDxiDFAConfTable=_AtmDxiDFAConfTable_Object((1,3,6,1,4,1,353,3,2,3))
if mibBuilder.loadTexts:atmDxiDFAConfTable.setStatus(_A)
_AtmDxiDFAConfEntry_Object=MibTableRow
atmDxiDFAConfEntry=_AtmDxiDFAConfEntry_Object((1,3,6,1,4,1,353,3,2,3,1))
atmDxiDFAConfEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:atmDxiDFAConfEntry.setStatus(_A)
_AtmDxiDFAConfIfIndex_Type=Integer32
_AtmDxiDFAConfIfIndex_Object=MibTableColumn
atmDxiDFAConfIfIndex=_AtmDxiDFAConfIfIndex_Object((1,3,6,1,4,1,353,3,2,3,1,1),_AtmDxiDFAConfIfIndex_Type())
atmDxiDFAConfIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atmDxiDFAConfIfIndex.setStatus(_A)
_AtmDxiDFAConfDfaIndex_Type=Dfa
_AtmDxiDFAConfDfaIndex_Object=MibTableColumn
atmDxiDFAConfDfaIndex=_AtmDxiDFAConfDfaIndex_Object((1,3,6,1,4,1,353,3,2,3,1,2),_AtmDxiDFAConfDfaIndex_Type())
atmDxiDFAConfDfaIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atmDxiDFAConfDfaIndex.setStatus(_A)
class _AtmDxiDFAConfAALType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('none',2),('aal34',3),('aal5',4)))
_AtmDxiDFAConfAALType_Type.__name__=_C
_AtmDxiDFAConfAALType_Object=MibTableColumn
atmDxiDFAConfAALType=_AtmDxiDFAConfAALType_Object((1,3,6,1,4,1,353,3,2,3,1,3),_AtmDxiDFAConfAALType_Type())
atmDxiDFAConfAALType.setMaxAccess(_F)
if mibBuilder.loadTexts:atmDxiDFAConfAALType.setStatus(_A)
_AtmDxiEnterprise_Type=ObjectIdentifier
_AtmDxiEnterprise_Object=MibScalar
atmDxiEnterprise=_AtmDxiEnterprise_Object((1,3,6,1,4,1,353,3,2,4),_AtmDxiEnterprise_Type())
atmDxiEnterprise.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:atmDxiEnterprise.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Dfa':Dfa,'atmForum':atmForum,'atmUniDxi':atmUniDxi,'atmDxi':atmDxi,'atmDxiConfTable':atmDxiConfTable,'atmDxiConfEntry':atmDxiConfEntry,_E:atmDxiConfIfIndex,'atmDxiConfMode':atmDxiConfMode,'atmDxiDFAConfTable':atmDxiDFAConfTable,'atmDxiDFAConfEntry':atmDxiDFAConfEntry,_G:atmDxiDFAConfIfIndex,_H:atmDxiDFAConfDfaIndex,'atmDxiDFAConfAALType':atmDxiDFAConfAALType,'atmDxiEnterprise':atmDxiEnterprise})