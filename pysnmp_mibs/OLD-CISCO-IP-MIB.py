_K='ckactDst'
_J='ckactSrc'
_I='actDst'
_H='actSrc'
_G='ipRouteDest'
_F='RFC1213-MIB'
_E='ipAdEntAddr'
_D='IP-MIB'
_C='OLD-CISCO-IP-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
local,=mibBuilder.importSymbols('CISCO-SMI','local')
ipAdEntAddr,=mibBuilder.importSymbols(_D,_E)
ipRouteDest,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Lip_ObjectIdentity=ObjectIdentity
lip=_Lip_ObjectIdentity((1,3,6,1,4,1,9,2,4))
_LipAddrTable_Object=MibTable
lipAddrTable=_LipAddrTable_Object((1,3,6,1,4,1,9,2,4,1))
if mibBuilder.loadTexts:lipAddrTable.setStatus(_A)
_LipAddrEntry_Object=MibTableRow
lipAddrEntry=_LipAddrEntry_Object((1,3,6,1,4,1,9,2,4,1,1))
lipAddrEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:lipAddrEntry.setStatus(_A)
_LocIPHow_Type=DisplayString
_LocIPHow_Object=MibTableColumn
locIPHow=_LocIPHow_Object((1,3,6,1,4,1,9,2,4,1,1,1),_LocIPHow_Type())
locIPHow.setMaxAccess(_B)
if mibBuilder.loadTexts:locIPHow.setStatus(_A)
_LocIPWho_Type=IpAddress
_LocIPWho_Object=MibTableColumn
locIPWho=_LocIPWho_Object((1,3,6,1,4,1,9,2,4,1,1,2),_LocIPWho_Type())
locIPWho.setMaxAccess(_B)
if mibBuilder.loadTexts:locIPWho.setStatus(_A)
_LocIPHelper_Type=IpAddress
_LocIPHelper_Object=MibTableColumn
locIPHelper=_LocIPHelper_Object((1,3,6,1,4,1,9,2,4,1,1,3),_LocIPHelper_Type())
locIPHelper.setMaxAccess(_B)
if mibBuilder.loadTexts:locIPHelper.setStatus(_A)
_LocIPSecurity_Type=Integer32
_LocIPSecurity_Object=MibTableColumn
locIPSecurity=_LocIPSecurity_Object((1,3,6,1,4,1,9,2,4,1,1,4),_LocIPSecurity_Type())
locIPSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:locIPSecurity.setStatus(_A)
_LocIPRedirects_Type=Integer32
_LocIPRedirects_Object=MibTableColumn
locIPRedirects=_LocIPRedirects_Object((1,3,6,1,4,1,9,2,4,1,1,5),_LocIPRedirects_Type())
locIPRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:locIPRedirects.setStatus(_A)
_LocIPUnreach_Type=Integer32
_LocIPUnreach_Object=MibTableColumn
locIPUnreach=_LocIPUnreach_Object((1,3,6,1,4,1,9,2,4,1,1,6),_LocIPUnreach_Type())
locIPUnreach.setMaxAccess(_B)
if mibBuilder.loadTexts:locIPUnreach.setStatus(_A)
_LipRouteTable_Object=MibTable
lipRouteTable=_LipRouteTable_Object((1,3,6,1,4,1,9,2,4,2))
if mibBuilder.loadTexts:lipRouteTable.setStatus(_A)
_LipRouteEntry_Object=MibTableRow
lipRouteEntry=_LipRouteEntry_Object((1,3,6,1,4,1,9,2,4,2,1))
lipRouteEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:lipRouteEntry.setStatus(_A)
_LocRtMask_Type=IpAddress
_LocRtMask_Object=MibTableColumn
locRtMask=_LocRtMask_Object((1,3,6,1,4,1,9,2,4,2,1,1),_LocRtMask_Type())
locRtMask.setMaxAccess(_B)
if mibBuilder.loadTexts:locRtMask.setStatus(_A)
_LocRtCount_Type=Integer32
_LocRtCount_Object=MibTableColumn
locRtCount=_LocRtCount_Object((1,3,6,1,4,1,9,2,4,2,1,2),_LocRtCount_Type())
locRtCount.setMaxAccess(_B)
if mibBuilder.loadTexts:locRtCount.setStatus(_A)
_LocRtUses_Type=Integer32
_LocRtUses_Object=MibTableColumn
locRtUses=_LocRtUses_Object((1,3,6,1,4,1,9,2,4,2,1,3),_LocRtUses_Type())
locRtUses.setMaxAccess(_B)
if mibBuilder.loadTexts:locRtUses.setStatus(_A)
_ActThresh_Type=Integer32
_ActThresh_Object=MibScalar
actThresh=_ActThresh_Object((1,3,6,1,4,1,9,2,4,4),_ActThresh_Type())
actThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:actThresh.setStatus(_A)
_ActLostPkts_Type=Integer32
_ActLostPkts_Object=MibScalar
actLostPkts=_ActLostPkts_Object((1,3,6,1,4,1,9,2,4,5),_ActLostPkts_Type())
actLostPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:actLostPkts.setStatus(_A)
_ActLostByts_Type=Integer32
_ActLostByts_Object=MibScalar
actLostByts=_ActLostByts_Object((1,3,6,1,4,1,9,2,4,6),_ActLostByts_Type())
actLostByts.setMaxAccess(_B)
if mibBuilder.loadTexts:actLostByts.setStatus(_A)
_LipAccountingTable_Object=MibTable
lipAccountingTable=_LipAccountingTable_Object((1,3,6,1,4,1,9,2,4,7))
if mibBuilder.loadTexts:lipAccountingTable.setStatus(_A)
_LipAccountEntry_Object=MibTableRow
lipAccountEntry=_LipAccountEntry_Object((1,3,6,1,4,1,9,2,4,7,1))
lipAccountEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:lipAccountEntry.setStatus(_A)
_ActSrc_Type=IpAddress
_ActSrc_Object=MibTableColumn
actSrc=_ActSrc_Object((1,3,6,1,4,1,9,2,4,7,1,1),_ActSrc_Type())
actSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:actSrc.setStatus(_A)
_ActDst_Type=IpAddress
_ActDst_Object=MibTableColumn
actDst=_ActDst_Object((1,3,6,1,4,1,9,2,4,7,1,2),_ActDst_Type())
actDst.setMaxAccess(_B)
if mibBuilder.loadTexts:actDst.setStatus(_A)
_ActPkts_Type=Integer32
_ActPkts_Object=MibTableColumn
actPkts=_ActPkts_Object((1,3,6,1,4,1,9,2,4,7,1,3),_ActPkts_Type())
actPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:actPkts.setStatus(_A)
_ActByts_Type=Integer32
_ActByts_Object=MibTableColumn
actByts=_ActByts_Object((1,3,6,1,4,1,9,2,4,7,1,4),_ActByts_Type())
actByts.setMaxAccess(_B)
if mibBuilder.loadTexts:actByts.setStatus(_A)
_ActViolation_Type=Integer32
_ActViolation_Object=MibTableColumn
actViolation=_ActViolation_Object((1,3,6,1,4,1,9,2,4,7,1,5),_ActViolation_Type())
actViolation.setMaxAccess(_B)
if mibBuilder.loadTexts:actViolation.setStatus(_A)
_ActAge_Type=TimeTicks
_ActAge_Object=MibScalar
actAge=_ActAge_Object((1,3,6,1,4,1,9,2,4,8),_ActAge_Type())
actAge.setMaxAccess(_B)
if mibBuilder.loadTexts:actAge.setStatus(_A)
_LipCkAccountingTable_Object=MibTable
lipCkAccountingTable=_LipCkAccountingTable_Object((1,3,6,1,4,1,9,2,4,9))
if mibBuilder.loadTexts:lipCkAccountingTable.setStatus(_A)
_LipCkAccountEntry_Object=MibTableRow
lipCkAccountEntry=_LipCkAccountEntry_Object((1,3,6,1,4,1,9,2,4,9,1))
lipCkAccountEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:lipCkAccountEntry.setStatus(_A)
_CkactSrc_Type=IpAddress
_CkactSrc_Object=MibTableColumn
ckactSrc=_CkactSrc_Object((1,3,6,1,4,1,9,2,4,9,1,1),_CkactSrc_Type())
ckactSrc.setMaxAccess(_B)
if mibBuilder.loadTexts:ckactSrc.setStatus(_A)
_CkactDst_Type=IpAddress
_CkactDst_Object=MibTableColumn
ckactDst=_CkactDst_Object((1,3,6,1,4,1,9,2,4,9,1,2),_CkactDst_Type())
ckactDst.setMaxAccess(_B)
if mibBuilder.loadTexts:ckactDst.setStatus(_A)
_CkactPkts_Type=Integer32
_CkactPkts_Object=MibTableColumn
ckactPkts=_CkactPkts_Object((1,3,6,1,4,1,9,2,4,9,1,3),_CkactPkts_Type())
ckactPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ckactPkts.setStatus(_A)
_CkactByts_Type=Integer32
_CkactByts_Object=MibTableColumn
ckactByts=_CkactByts_Object((1,3,6,1,4,1,9,2,4,9,1,4),_CkactByts_Type())
ckactByts.setMaxAccess(_B)
if mibBuilder.loadTexts:ckactByts.setStatus(_A)
_CkactViolation_Type=Integer32
_CkactViolation_Object=MibTableColumn
ckactViolation=_CkactViolation_Object((1,3,6,1,4,1,9,2,4,9,1,5),_CkactViolation_Type())
ckactViolation.setMaxAccess(_B)
if mibBuilder.loadTexts:ckactViolation.setStatus(_A)
_CkactAge_Type=TimeTicks
_CkactAge_Object=MibScalar
ckactAge=_CkactAge_Object((1,3,6,1,4,1,9,2,4,10),_CkactAge_Type())
ckactAge.setMaxAccess(_B)
if mibBuilder.loadTexts:ckactAge.setStatus(_A)
_ActCheckPoint_Type=Integer32
_ActCheckPoint_Object=MibScalar
actCheckPoint=_ActCheckPoint_Object((1,3,6,1,4,1,9,2,4,11),_ActCheckPoint_Type())
actCheckPoint.setMaxAccess('read-write')
if mibBuilder.loadTexts:actCheckPoint.setStatus(_A)
_IpNoaccess_Type=Counter32
_IpNoaccess_Object=MibScalar
ipNoaccess=_IpNoaccess_Object((1,3,6,1,4,1,9,2,4,12),_IpNoaccess_Type())
ipNoaccess.setMaxAccess(_B)
if mibBuilder.loadTexts:ipNoaccess.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'lip':lip,'lipAddrTable':lipAddrTable,'lipAddrEntry':lipAddrEntry,'locIPHow':locIPHow,'locIPWho':locIPWho,'locIPHelper':locIPHelper,'locIPSecurity':locIPSecurity,'locIPRedirects':locIPRedirects,'locIPUnreach':locIPUnreach,'lipRouteTable':lipRouteTable,'lipRouteEntry':lipRouteEntry,'locRtMask':locRtMask,'locRtCount':locRtCount,'locRtUses':locRtUses,'actThresh':actThresh,'actLostPkts':actLostPkts,'actLostByts':actLostByts,'lipAccountingTable':lipAccountingTable,'lipAccountEntry':lipAccountEntry,_H:actSrc,_I:actDst,'actPkts':actPkts,'actByts':actByts,'actViolation':actViolation,'actAge':actAge,'lipCkAccountingTable':lipCkAccountingTable,'lipCkAccountEntry':lipCkAccountEntry,_J:ckactSrc,_K:ckactDst,'ckactPkts':ckactPkts,'ckactByts':ckactByts,'ckactViolation':ckactViolation,'ckactAge':ckactAge,'actCheckPoint':actCheckPoint,'ipNoaccess':ipNoaccess})